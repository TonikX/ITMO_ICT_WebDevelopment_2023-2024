# Задание №4

Реализуем страницу профиля с разделением на колоду (4 активные карты) и коллекцию (все остальные карты). Данные будем получать из стора, при необходимости будет отправлять запрос на сервер на смену карт в колоде и коллекции. Сделаем возможность заменять карты при помощи анимаций.

## Клиент (panels/profile/index.ts):

```typescript
import styled from "@emotion/styled";
import { replace, useLocation, useMeta } from "@itznevikat/router";
import { NavIdProps, Panel } from "@vkontakte/vkui";
import anime from "animejs";
import React, {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
} from "react";
import { useDispatch } from "react-redux";

import Balance from "@/components/Balance";
import { CardItem, getCardsData } from "@/data/cards";
import { cardPopupSound, cardReplaceSound } from "@/data/sounds/interface";
import { images } from "@/data/url";
import { tutorialReplace } from "@/modals/modalTutorial/blockedNavigation";
import { DataTutorialIds } from "@/modals/modalTutorial/stepsConfig";
import {
  setCollection as setReduxCollection,
  setDeck as setReduxDeck,
} from "@/reducers/user.reducer";
import { RootState, useSelector } from "@/store";
import { request } from "@/utils/request";

import { animateSwapCard } from "./Cards/animations";
import CollectionBlock from "./CollectionBlock";
import DeckBlock from "./DeckBlock";
import HeaderBlock from "./HeaderBlock";

export type DeckTabType = "deck" | "emotions" | "statistics";
type CardContextType = {
  deck: CardItem[];
  collection: CardItem[];
  expendedCard?: CardItem;
  selectedCard?: CardItem;
};

const CardContext = React.createContext<CardContextType>({
  deck: [],
  collection: [],
});

type InteractionContextType = {
  isDisabledInteraction: boolean;
  setIsDisabledInteraction: (value: boolean) => void;
};

const InteractionContext = React.createContext<InteractionContextType>({
  isDisabledInteraction: false,
  setIsDisabledInteraction: () => void 0,
});

const Root = styled(Panel, {
  shouldForwardProp: (prop) => prop !== "scrollBlocked",
})<{ scrollBlocked: boolean }>`
  position: relative;

  background: url(${images.background.profile}) center;
  background-size: contain;
  background-attachment: fixed;
  overflow: hidden;

  &.vkuiPanel::after {
    background-color: transparent !important;
  }

  & > .vkuiPanel__in {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: transparent;

    overflow: ${(props) => (props.scrollBlocked ? "hidden" : "scroll")};

    max-height: 100vh;
    &::-webkit-scrollbar {
      width: 0px;
      height: 0px;
    }
  }

  &:after {
    background-color: transparent;
  }

  user-select: none;
`;

type ProfilePanelProps = NavIdProps &
  Omit<React.ComponentPropsWithRef<typeof Root>, "children" | "scrollBlocked">;

function ProfilePanel(props: ProfilePanelProps): JSX.Element {
  const userState = useSelector((state: RootState) => state.User);
  const dispatch = useDispatch();

  const { pathname } = useLocation();
  const meta = useMeta();

  const [cards, setCards] = useState({
    deck: getCardsData(userState.deck, { inDeck: true }),
    collection: getCardsData(userState.collection, {}),
  });
  const [selectedTab, setSelectedTab] = React.useState<DeckTabType>("deck");

  const collectionRef = useRef<HTMLDivElement>(null);
  const [expendedCard, setExpendedCard] = useState<CardItem>();
  const [selectedCard, setSelectedCard] = useState<CardItem>();
  const [isDisabledInteraction, setIsDisabledInteraction] = useState(false);

  // Функция для сохранения изменений в Redux
  useEffect(() => {
    dispatch(
      setReduxDeck(cards.deck as [CardItem, CardItem, CardItem, CardItem])
    );
    dispatch(setReduxCollection(cards.collection));
  }, [cards]);

  // Обработчик нажатия вне карточек
  const handleRootClick = () => {
    if (isDisabledInteraction) return;

    cardPopupSound.play();
    setExpendedCard(undefined);
    setSelectedCard(undefined);
    resetCollectionHeight();
  };

  // Обработчик нажатия по карточке
  const handleCardClick = (card: CardItem) => {
    if (isDisabledInteraction) return;

    cardPopupSound.play();
    setExpendedCard(card);
    setSelectedCard(undefined);
    resetCollectionHeight();
  };

  // Обработчик нажатия кнопки "Выбрать"
  const handleSelectClick = (card: CardItem) => {
    if (isDisabledInteraction) return;

    cardPopupSound.play();
    setSelectedCard(card);
    setIsDisabledInteraction(true);

    anime({
      targets: "#cards",
      height: 0,
      delay: 300,
      duration: 300,
      easing: "easeInQuad",
      complete: () => setIsDisabledInteraction(false),
    });
  };

  // Обработчик нажатия кнопки "Информация"
  const handleShowDescription = (card: CardItem) => {
    if (isDisabledInteraction) return;

    cardPopupSound.play();
    replace(`${pathname}?modal=cardInfo`, { unit: card.entity });
  };

  // Обработчик нажатия
  const handleCardSwap = (cardToCollection: CardItem, cardToDock: CardItem) => {
    if (isDisabledInteraction) return;
    // Отправляем запрос на сервер для изменения позици карточки
    request({
      auth: true,
      method: "user/replaceCard",
      params: {
        entity: cardToDock.entity,
        position:
          cards.deck.findIndex((card) => card.id === cardToCollection.id) + 1,
      },
    });

    cardReplaceSound.play();
    setIsDisabledInteraction(true);

    // Анимация перемещения карточек
    animateSwapCard(cardToCollection, () => {
      setIsDisabledInteraction(false);
      setExpendedCard(undefined);
      setSelectedCard(undefined);
      resetCollectionHeight();

      // Изменяем список карточек в сторе
      setCards((cards) => {
        const deck = cards.deck.map((card) =>
          card.id === cardToCollection.id ? cardToDock : card
        );
        const collection = cards.collection.map((card) =>
          card.id === cardToDock.id ? cardToCollection : card
        );
        return { deck, collection };
      });
    });
  };

  const cardContextValue = useMemo(
    () => ({
      ...cards,
      expendedCard,
      selectedCard,
      isDisabledInteraction,
    }),
    [cards, expendedCard, selectedCard, isDisabledInteraction]
  );

  return (
    <CardContext.Provider value={cardContextValue}>
      <InteractionContext.Provider
        value={{ isDisabledInteraction, setIsDisabledInteraction }}
      >
        <Root
          onClick={handleRootClick}
          {...props}
          scrollBlocked={selectedCard !== undefined}
        >
          <Balance />
          <HeaderBlock />
          <DeckBlock
            onCardSwap={handleCardSwap}
            onShowDescription={handleShowDescription}
            data-tutorial-step={DataTutorialIds.DeckBlock}
            selectedTab={selectedTab}
            setSelectedTab={setSelectedTab}
          />
          {selectedTab === "deck" && (
            <CollectionBlock
              onCardClick={handleCardClick}
              onSelectClick={handleSelectClick}
              onShowDescription={handleShowDescription}
              ref={collectionRef}
            />
          )}
        </Root>
      </InteractionContext.Provider>
    </CardContext.Provider>
  );
}

export default ProfilePanel;
export { CardContext, InteractionContext };
```
