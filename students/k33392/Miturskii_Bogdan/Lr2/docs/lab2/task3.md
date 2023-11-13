# Задание №3

Реализуем запрос ползволяющий пользователю получить данные по рейтингу своих друзей

## Сервер (hub/routes/friendsRating.ts):

```typescript
import { Response } from "express";
import { IUser, Users } from "@src/models/Users";
import { IRatingItem, IVKUser } from "../../processes/rating";
import { IGetUserIDAuthInfoRequest } from "../../types/request";
import axios from "axios";

export default async function (req: IGetUserIDAuthInfoRequest, res: Response) {
  // Проверяем наличие записи в кеше
  const redisKey = `friendsRating${req.userID}`;
  const cache = await redis.get(redisKey);

  if (cache) {
    res.json(JSON.parse(cache));
    return;
  }

  // Парсим полученные с фронтенда id друзей
  const ids = String(req.query.list).split(",");
  if (ids.length > 10000)
    return res.status(400).json({ error: "Максильмальное количество друзей" });

  // Находим друзей в общей базе данынх
  let dbUsers: IUser[];
  try {
    dbUsers = await Users.find({ _id: { $in: [req.userID, ...ids] } })
      .sort({ rating: -1 })
      .lean();
  } catch {
    return res.status(400).json({ error: "Некорректно введен список друзей" });
  }

  if (dbUsers.length <= 1) return res.status(400).json({ error: "no_friends" });

  /**
   * Одним циклом собираем как можно больше информации про топ друзей пользователя
   *
   * top100 - массив с первыми 100 участниками топа
   * currentUser - объект с информацией о пользователе (будет закреплен снизу в топе)
   * vkIds - id для запроса аватара и имени из ВК
   * objLinks - ссылки на объекты для удобства
   */
  const top100 = [] as IRatingItem[];
  let currentUser: IRatingItem | null = null;
  const vkIds = [] as number[];
  const objLinks = {} as Record<number, IRatingItem>;
  for (let index = 0; index < dbUsers.length; index++) {
    const user = dbUsers[index];

    const userObject: IRatingItem = {
      _id: user._id,
      position: index + 1,
      rating: user.rating,
      photo_100: "",
      online_status: "offline",
      name: "",
    };

    if (index < 100) top100.push(userObject);
    if (user._id === req.userID) currentUser = userObject;
    if (index < 100 || user._id === req.userID) {
      vkIds.push(user._id);
      objLinks[user._id] = userObject;
    }

    // Если мы уже набрали весь топ-100 и нашли позицию текущего пользователя, то дальше идти по циклу смысла нет
    if (top100.length === 100 && currentUser) break;
  }

  const { data: vkUsersResponse } = await axios.get(
    `https://api.vk.com/method/users.get?access_token=${
      process.env.APP_TOKEN
    }&v=5.131&user_ids=${vkIds.join(",")}&fields=photo_100,online&lang=ru`
  );
  vkUsersResponse.response.forEach((user: IVKUser) => {
    objLinks[user.id].name = `${user.first_name} ${user.last_name}`;
    objLinks[user.id].online_status = user.online
      ? user.online_mobile
        ? "mobile"
        : "online"
      : "offline";
    objLinks[user.id].photo_100 = user.photo_100;
  });

  // Отправляем на фронтенд сформированный топ
  const response = {
    items: top100,
    user: currentUser,
  };
  res.json(response);

  // Кешируем полученный список
  redis.setex(redisKey, 10 * 60, response);
}
```
