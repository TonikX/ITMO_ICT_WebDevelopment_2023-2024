# Задание №4

Реализуем роут позволяющий работать с колодой карт пользователя. (Заменять карты местами)

## Сервер (hub/routes/replaceCard.ts):

```typescript
import { IGetUserIDAuthInfoRequest } from "../../types/request";
import { findUser } from "@src/utils/findUser";
import { Response } from "express";
import { CardsData, DeckCardsTypes, CardUnits } from "@src/data/cards";

function isEntityType(str: unknown): str is CardUnits {
  if (typeof str === "string") return str in CardUnits;
  return false;
}

export default async function (req: IGetUserIDAuthInfoRequest, res: Response) {
  const entity = req.query.entity;

  // Проводим проверки на возможность перестановки карт местами
  if (!isEntityType(entity))
    return res.status(400).json({ error: "Слот в колоде не найден" });

  const position = Number(req.query.position);
  const cardData = CardsData[entity];

  if (position > 4 || position < 1 || Number.isNaN(position)) {
    return res.status(400).json({ error: "Слот в колоде не найден" });
  }

  if (
    cardData &&
    position !== 0 &&
    cardData.type !== DeckCardsTypes[position - 1] &&
    DeckCardsTypes[position - 1] !== null
  ) {
    return res.status(400).json({
      error: `Данный тип карты не может быть расположен в слоте ${position}`,
    });
  }

  const user = await findUser(req.userID);
  if (!user) return;

  let cardFound = false;
  let previousCardFound = false;
  for (const card of user.cards) {
    if (card.position === position && card.entity !== entity) {
      card.position = undefined;
      previousCardFound = true;

      if (cardFound) break;
      continue;
    }

    if (card.entity === entity) {
      if (typeof card.parts === "number") break;

      card.position = position;
      cardFound = true;

      if (previousCardFound) break;
    }
  }

  if (!cardFound) return res.status(400).json({ error: "Карта заблокирована" });

  await user.save();

  // Отправляем положительный ответ если карту заменить можно
  res.status(200).json({ ok: true });
}
```
