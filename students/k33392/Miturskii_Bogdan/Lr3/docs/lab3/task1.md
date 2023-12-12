# Задание №1

Подготовим коллекцию User для хранения данных игрока на сервере

## Сервер (hub/models/Users.ts):

```typescript
import mongoose, {
  HydratedDocument,
  ObjectId,
  PopulatedDoc,
  Schema,
} from "mongoose";
import { IEntity } from "../data/cards";
import { ILobby } from "./Lobbies";
import { IChestTypes } from "../data/chests";
import { StoreProducts } from "../data/shop";
import { MIN_RATING } from "@src/data/rating";

export type Currency = "coins" | "voices";

// Тип карты из колоды
export type ICard = {
  entity: IEntity;
  parts?: number;
  position?: number;
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

// Схема карт являющаяся частью схемы профиля игрока
const CardSchema = new Schema<ICard>({
  entity: {
    type: String,
    required: true,
  },
  parts: Number,
  position: Number,
});

// Типы для сундука в базе данных
export type IChest =
  | { empty: true; _id?: ObjectId }
  | ({
      empty?: false;
      _id?: ObjectId;
      type: IChestTypes;
      adWatchedTimes: number;
    } & (
      | {
          status: "idle";
        }
      | {
          status: "opening";
          willOpenAt: number;
        }
    ));

export type IChestDocs = [
  HydratedDocument<IChest>,
  HydratedDocument<IChest>,
  HydratedDocument<IChest>,
  HydratedDocument<IChest>
];

const ChestSchema = new Schema<IChest>({
  type: String,
  status: String,
  willOpenAt: Number,
  empty: Boolean,
  adWatchedTimes: {
    type: Number,
    default: 0,
    required: true,
  },
});

// Типы итогового интерфейса пользователя
export interface IUser {
  _id: number;
  name: string;
  photo_200: string;
  registrationDate: Date;
  ban?: boolean;
  cards: ICard[];
  balance: number;
  history: any[];
  chests: [IChest, IChest, IChest, IChest];
  rating: number;

  stats: {
    draws: number;
    wins: number;
    losses: number;
  };
  lobby: PopulatedDoc<ILobby>;

  bonuses: Bonuses;
  isTutorialPassed: boolean;
  shop: {
    lastUpdate: number;
    boughtProducts: StoreProducts[];
    chest: {
      currency: Currency;
      chestType: IChestTypes | "";
    };

    cardFragment: {
      currency: Currency;
      card: IEntity | "";
    };
  };

  tasks: {
    current: string[];
    completed: string[];
    progress: Record<string, number>;
    nextUpdateAt: number;
    lastTasksMessageId?: number;
    madeProgress?: boolean;
  };
}

// Стартовые карты получаемые пользователем при входе в игру
const defaultCards: ICard[] = [
  {
    entity: "sheep",
    position: 1,
  },
  {
    entity: "farm",
    position: 2,
  },
  {
    entity: "pasture",
    position: 3,
  },
  {
    entity: "bigSheep",
    position: 4,
  },
  {
    entity: "teslaTower",
  },
  {
    entity: "bee",
  },
  {
    entity: "doubleFarm",
    parts: 1,
  },
];

// Схема пользоавтеля через Mongoose
const UserSchema = new Schema<IUser>({
  _id: { index: true, required: true, type: Number },
  ban: {
    type: Boolean,
    required: false,
  },
  name: {
    type: "string",
    required: true,
  },
  photo_200: {
    type: "string",
    required: true,
  },
  registrationDate: {
    type: Date,
  },
  cards: {
    type: [CardSchema],
    required: true,
    default: defaultCards,
  },
  balance: {
    type: Number,
    required: true,
    default: 0,
  },
  history: {
    type: [],
    required: true,
    default: [],
  },
  stats: {
    wins: {
      type: Number,
      default: 0,
      required: true,
    },
    losses: {
      type: Number,
      default: 0,
      required: true,
    },
    draws: {
      type: Number,
      default: 0,
      required: true,
    },
  },

  chests: {
    type: [ChestSchema],
    default: [
      { empty: true },
      { empty: true },
      { empty: true },
      { empty: true },
    ],
    required: true,
  },
  rating: {
    type: Number,
    default: MIN_RATING,
    required: true,
    index: -1,
  },

  lobby: { type: Schema.Types.ObjectId, ref: "lobbies" },

  bonuses: {
    daily: {
      type: Number,
      default: 0,
      required: true,
    },
    subGroup: {
      type: Boolean,
      default: false,
      required: true,
    },
    joinChat: {
      type: Boolean,
      default: false,
      required: true,
    },
    notificationApp: {
      type: Boolean,
      default: false,
      required: true,
    },
    notificationBot: {
      type: Boolean,
      default: false,
      required: true,
    },
    addToFavorites: {
      type: Boolean,
      default: false,
      required: true,
    },
    rewardedGift: {
      lastUpdate: {
        type: Number,
        default: Date.now(),
        required: true,
      },
      adWatchedTimes: {
        type: Number,
        default: 0,
        required: true,
      },
    },
  },
  isTutorialPassed: {
    type: Boolean,
    default: false,
    required: true,
  },
  shop: {
    lastUpdate: {
      type: Number,
      default: 0,
      required: true,
    },
    boughtProducts: {
      type: Object,
      default: [],
      required: true,
    },
    chest: {
      chestType: {
        type: String,
        default: "",
      },
      currency: {
        type: String,
        default: "coins",
      },
    },
    cardFragment: {
      card: {
        type: String,
        default: "",
      },
      currency: {
        type: String,
        default: "coins",
      },
    },
  },
  tasks: {
    completed: {
      type: [String],
      required: true,
      default: [],
    },
    current: {
      type: [String],
      required: true,
      default: [],
    },
    progress: {
      type: {},
      default: {},
      required: true,
    },
    nextUpdateAt: {
      type: Number,
      required: true,
      default: 0,
    },
    lastTasksMessageId: {
      type: Number,
    },
    madeProgress: { type: Boolean },
  },
});

export const Users = mongoose.model("users", UserSchema);
```
