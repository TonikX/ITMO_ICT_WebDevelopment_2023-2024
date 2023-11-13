# Задание №2

Реализуем запрос ползволяющий пользователю получить данные по общему рейтингу пользователей

## Сервер (hub/routes/connect.ts):

```typescript
import axios from "axios";
import { Response } from "express";
import { IRatingItem, IVKUser } from "../../processes/rating";
import { IGetUserIDAuthInfoRequest } from "../../types/request";
import { findUser } from "@src/utils/findUser";

// Время следующего обновления рейтинга
let nextRatingUpdate: number;
// Локальная запись рейтинга во избежание лишних запросов к бд
let rating: { items: IRatingItem[]; positions: number[] };

export default async function (req: IGetUserIDAuthInfoRequest, res: Response) {
  const user = await findUser(req.userID);
  if (!user) return;

  // Достаем обновленный рейтинг из redis, если прошло время обновления рейтинга
  if (!rating || nextRatingUpdate <= Date.now())
    updatingRating: {
      const updatedRating = await redis.get("rating");
      if (!updatedRating && !rating)
        return res.status(400).json({ error: "Рейтинг еще не загружен" });
      if (!updatedRating) break updatingRating;
      rating = JSON.parse(updatedRating);
      nextRatingUpdate = Date.now() + 60 * 1000;
    }

  // Находим позицию пользователя
  const position = rating.positions.indexOf(user._id);
  // Прописываем свою позицию отдельно от топ 100
  const userInRating: IRatingItem = {
    _id: user._id,
    name: user.name,
    photo_100: user.photo_200,
    position: position === -1 ? 10001 : position + 1,
    online_status: "offline",
    rating: user.rating,
  };

  res.json({
    items: rating.items,
    user: userInRating,
  });
}
```
