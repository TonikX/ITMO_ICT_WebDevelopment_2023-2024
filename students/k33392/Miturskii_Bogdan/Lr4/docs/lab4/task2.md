# Задание №2

Реализуем хранилище пользовательских данных на клиенте с помощью redux store.

## Клиент (store/user.reducer.ts):

```typescript
import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";
import { IChestTypes } from "@/panels/ChestOpening/prize";
import { CardRarities } from "@/data/cards";
import { request } from "@/utils/request";

type StatsState = {
  wins: number;
  losses: number;
  draws: number;
};

type Bonuses = {
  daily: number;
  subGroup: boolean;
  joinChat: boolean;
  notificationApp: boolean;
  notificationBot: boolean;
  addToFavorites: boolean;
  rewardedGift: {
    lastUpdate: number;
    adWatchedTimes: number;
  };
};

type HistoryState = {
  id: number;
  userResponse: {
    rating: number;
    chest: IChestTypes;
    status: "win" | "lose" | "draw";
  };
  opponentInfo: {
    id: number;
    photo_200: string;
  };
  date: number;
};

export type IChest = {
  type: IChestTypes;
  willOpenAt?: number;
  status: "opening" | "idle";
  adWatchedTimes: number;
} | null;

export type EntityType =
  | "bigSheep"
  | "crashedPlane"
  | "deadFarm"
  | "doubleFarm"
  | "farm"
  | "fastSheep"
  | "pasture"
  | "sheep"
  | "empty1"
  | "empty2"
  | "empty3"
  | "empty4";

export type DeckItem = { entity: EntityType } & (
  | {
      blocked: true;
      part: number;
      partMax?: number; // Для элемента карты
    }
  | {
      blocked?: false;
    }
);

export type Lottery = {
  endsAt: number;
  postLink: string;
  imageLink: string;
} | null;

export type UserState = {
  _id: number;
  name: string;
  balance: number;
  stats: StatsState;
  deck: [DeckItem, DeckItem, DeckItem, DeckItem];
  photo_200: string;
  history: HistoryState[] | [];
  collection: DeckItem[];
  isToken?: boolean;
  chests: [IChest, IChest, IChest, IChest];
  lobby?: {
    _id: number;
    url: string;
  };
  bonuses: Bonuses;
  rating: number;
  isTutorialPassed: boolean;
  shop: IShop;
  isShopLoading: boolean;
  lottery?: Lottery;
};

export type Coin = Extract<
  StoreProducts,
  StoreProducts.coins | StoreProducts.heapCoins | StoreProducts.bigHeapCoins
>;

export interface IShop {
  boughtProducts: StoreProducts[];
  chest: { chestType: IChestTypes | null; currency: "voices" | "coins" };
  cardFragment: { card: string | null; currency: "voices" | "coins" };
  prices: {
    coins: Record<Coin, number>;
    chests: Record<IChestTypes, { coins: number; voices: number }>;
    cards: Record<CardRarities, { coins: number; voices: number }>;
  };
  nextShopUpdate: number;
  promotion?: {
    title: string;
    description: string;
    endsAt: number;
    discounts: {
      voices: number;
      coins: number;
    };
  };
  serverDateNow: number;
}

export type ShopPrices = IShop["prices"];

const initialState: UserState = {
  _id: 0,
  name: "",
  photo_200: "",
  balance: 0,
  history: [],
  stats: {
    wins: 0,
    losses: 0,
    draws: 0,
  },
  deck: [
    { entity: "empty1" },
    { entity: "empty2" },
    { entity: "empty3" },
    { entity: "empty4" },
  ],
  collection: [],
  chests: [null, null, null, null],
  bonuses: {
    daily: 0,
    subGroup: false,
    joinChat: false,
    notificationApp: false,
    notificationBot: false,
    addToFavorites: false,
    rewardedGift: {
      lastUpdate: 0,
      adWatchedTimes: 0,
    },
  },
  rating: 0,
  isTutorialPassed: false,
  shop: {
    boughtProducts: [],
    chest: { chestType: null, currency: "coins" },
    cardFragment: { card: null, currency: "coins" },
    prices: {
      coins: {
        coins: 0,
        heapCoins: 0,
        bigHeapCoins: 0,
      },
      chests: {
        common: { coins: 0, voices: 0 },
        magic: { coins: 0, voices: 0 },
        legendary: { coins: 0, voices: 0 },
      },
      cards: {
        common: { coins: 0, voices: 0 },
        rare: { coins: 0, voices: 0 },
        epic: { coins: 0, voices: 0 },
        legendary: { coins: 0, voices: 0 },
      },
    },
    nextShopUpdate: 0,
    serverDateNow: Date.now(),
  },
  isShopLoading: false,
  lottery: undefined,
};

export enum StoreProducts {
  discontCard = "discontCard",
  discontChest = "discontChest",
  magicChest = "magicChest",
  commonChest = "commonChest",
  legendaryChest = "legendaryChest",
  coins = "coins",
  heapCoins = "heapCoins",
  bigHeapCoins = "bigHeapCoins",
}

const transfromOpenTime = (obj: IChest[]) => {
  const now = Date.now();
  obj.forEach((chest) => {
    if (!chest || chest.status !== "opening" || chest.willOpenAt === undefined)
      return;
    chest.willOpenAt += now;
  });
};

export const fetchShop = createAsyncThunk(
  "User/setShop",
  async function (_, { dispatch }) {
    const shopInfo = await request<IShop>({
      method: "shop/get",
      params: { getShop: true },
    });
    const serverTimeDif = shopInfo.serverDateNow - Date.now();
    // Переформатируем время под локальное
    shopInfo.nextShopUpdate -= serverTimeDif;
    if (shopInfo.promotion?.endsAt) shopInfo.promotion.endsAt -= serverTimeDif;

    dispatch(
      setShop({
        ...shopInfo,
        nextShopUpdate: shopInfo.nextShopUpdate,
      })
    );
  }
);

const UserSlice = createSlice({
  name: "User",
  initialState,
  reducers: {
    setUser(state: any, action: PayloadAction<any>) {
      if (action.payload?.chests) transfromOpenTime(action.payload.chests);
      Object.keys(action.payload).forEach((key) => {
        state[key as keyof UserState] = action.payload[key as keyof UserState];
      });
    },
    setBalance(state: UserState, action: PayloadAction<number>) {
      state.balance = action.payload;
    },
    setBonuses(state: UserState, action: PayloadAction<Bonuses>) {
      state.bonuses = action.payload;
    },
    setDeck(
      state: UserState,
      action: PayloadAction<[DeckItem, DeckItem, DeckItem, DeckItem]>
    ) {
      state.deck = action.payload;
    },
    setCollection(state: UserState, action: PayloadAction<DeckItem[]>) {
      state.collection = action.payload;
    },
    setChestStatus(
      state: UserState,
      action: PayloadAction<{
        index: number;
        status: "empty" | "opening";
      }>
    ) {
      const chest = state.chests[action.payload.index];
      if (chest === null) return;

      if (action.payload.status === "opening") {
        state.chests[action.payload.index] = {
          status: action.payload.status,
          type: chest.type,
          adWatchedTimes: chest.adWatchedTimes,
        };
      }

      if (action.payload.status === "empty") {
        state.chests[action.payload.index] = null;
      }
    },
    setChests(state: UserState, action: PayloadAction<UserState["chests"]>) {
      transfromOpenTime(action.payload);
      state.chests = action.payload;
    },
    changeDeck(
      state: UserState,
      action: PayloadAction<{ index: number; card: DeckItem }>
    ) {
      state.deck[action.payload.index] = action.payload.card;
    },
    changeCollection(
      state: UserState,
      action: PayloadAction<{ index: number; card: DeckItem }>
    ) {
      state.collection[action.payload.index] = action.payload.card;
    },
    setUserLobby(
      state: UserState,
      action: PayloadAction<{ url: string; _id: any }>
    ) {
      state.lobby = action.payload;
    },
    completeTutorial(state: UserState) {
      state.isTutorialPassed = true;
    },
    startTutorial(state: UserState) {
      state.isTutorialPassed = false;
    },
    setShop(state: UserState, action: PayloadAction<IShop>) {
      state.shop = action.payload;
      if (action.payload.nextShopUpdate)
        state.shop.nextShopUpdate += Date.now();
    },
    setDiscontProducts(
      state: UserState,
      action: PayloadAction<{
        chest: IShop["chest"];
        cardFragment: IShop["cardFragment"];
      }>
    ) {
      state.shop.chest = action.payload.chest;
      state.shop.cardFragment = action.payload.cardFragment;
    },
    setBoughtProducts(
      state: UserState,
      action: PayloadAction<StoreProducts[]>
    ) {
      state.shop.boughtProducts = action.payload;
    },
    setShopLoading(state: UserState, action: PayloadAction<boolean>) {
      state.isShopLoading = action.payload;
    },
    setLottery(state: UserState, action: PayloadAction<Lottery>) {
      state.lottery = action.payload;
      if (state.lottery) {
        state.lottery.endsAt += Date.now();
      }
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchShop.pending, (state) => {
        state.isShopLoading = true;
      })
      .addCase(fetchShop.fulfilled, (state) => {
        state.isShopLoading = false;
      });
  },
});

export default UserSlice.reducer;
export const {
  setUser,
  setBalance,
  setDeck,
  setCollection,
  changeDeck,
  changeCollection,
  setChestStatus,
  setChests,
  setUserLobby,
  setBonuses,
  completeTutorial,
  setShop,
  setShopLoading,
  setBoughtProducts,
  setDiscontProducts,
  setLottery,
  startTutorial,
} = UserSlice.actions;
```
