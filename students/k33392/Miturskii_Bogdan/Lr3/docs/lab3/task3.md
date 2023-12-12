# Задание №3

Реализуем роут возвращающий базовые данные пользователя.

Для начала реализуем функцию findUser которая будет доставть пользователя из базы если он есть и создать, если ещё нет.

## Сервер (hub/utils/findUser.ts):

```typescript
import { Users } from "../models/Users";
import { getUsersInfo } from "./vkapi";
import "../models/Lobbies";
import { recordUserAction } from "@/instances/hub/src/utils/recordUserAction";
import { IGetUserIDAuthInfoRequest } from "@/instances/hub/src/types/request";

export const findUser = async (
  id: number | string,
  req?: IGetUserIDAuthInfoRequest
) => {
  try {
    let user = await Users.findOne({ _id: id });
    if (!user) {
      // Запрашиваем данные пользователя из ВКонтакте (аватар, имя, фамилию)
      const usersInfo = await getUsersInfo(Number(id));
      if (!usersInfo) {
        throw new Error("failed to get vk user info for create");
      }

      const userInfo = usersInfo[0];
      const date = new Date();
      let user = await Users.create({
        _id: id,
        name: userInfo.name,
        photo_200: userInfo.photo,
        registrationDate: date.toISOString(),
      });

      return user;
    }

    return user;
  } catch (e) {
    console.log("Find User Error", e);
  }
};
```

Теперь реализуем саму функцию которая будет возвращать базовые данные пользователя.

## Сервер (hub/routes/user/getUser.ts):

```typescript
import { IGetUserIDAuthInfoRequest } from "../../types/request";
import { findUser } from "@src/utils/findUser";
import { Response } from "express";
import { IChestDocs, Users } from "@/src/models/Users";
import { getCollection } from "../../utils/getCardsInfo";
import { MIN_RATING } from "@src/data/rating";
import { getUsersInfo, group } from "@/src/utils/vkapi";
import { findShop } from "@/src/utils/findShop";
import { shopContentUpdate } from "../shop/getContent";

import { recordUserAction } from "../../utils/recordUserAction";
import {
  convertTasksToText,
  generateTasks,
} from "@/instances/bot/src/services";
import { format } from "util";
import { OLD_USERS_INTRODUCING, REMINDER } from "@/instances/bot/src/config";
import { TasksListKeyboard } from "@/instances/bot/src/config/keyboards";
import { refreshRewardedGiftTime } from "../../utils/refreshRewardedGiftTime";

export default async function (req: IGetUserIDAuthInfoRequest, res: Response) {
  // Достанем пользователя из базы данных
  const user = await findUser(req.userID, req);
  if (!user) return;

  // Обновляем аватар, имя и прочие данные пользователя при перезаходе в мини-приложение
  const vkUsersInfo = await getUsersInfo(user._id);
  if (!vkUsersInfo?.length) {
    res.status(500).json({
      message: "failed to get vk user info",
    });
    return;
  }

  const vkUserInfo = vkUsersInfo[0];

  if (user.photo_200 != vkUserInfo.photo || user.name != vkUserInfo.name) {
    user.photo_200 = vkUserInfo.photo;
    user.name = vkUserInfo.name;
    await user.save();
  }

  const { deck, collection } = getCollection(user.cards);
  const { shop, ...userObject } = user.toObject();

  // Формируем ответ который отправим на фронтенд
  const response = {
    ...userObject,
    cards: undefined,
    collection,
    deck,
    chests: (user.chests as IChestDocs).map((doc) => {
      const { _id, willOpenAt, ...chest } = doc.toObject() as any;
      return chest.empty
        ? null
        : {
            ...chest,
            willOpenAt:
              willOpenAt === undefined ? undefined : willOpenAt - Date.now(),
          };
    }),
  };

  res.status(200).json(response);
}
```
