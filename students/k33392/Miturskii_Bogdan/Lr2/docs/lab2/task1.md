# Задание №1

Реализуем алгоритм сортировки пользователей по количеству их кубков в базе данных (MongoDB). Полученный список будем обрабатывать для получения имени пользователя, а также его аватара из ВК, а затем кешировать посредством Redis для избежания лишней нагрузки.

## Сервер (hub/processes/rating.ts):

```typescript
import cron from "node-cron";
import { Users } from "@src/models/Users";
import axios from "axios";

export type IRatingItem = {
  photo_100?: string;
  position: number;
  online_status?: "online" | "mobile" | "offline";
  _id: number;
  name?: string;
  rating: number;
};

export type IVKUser = {
  id: number;
  first_name: string;
  last_name: string;
  photo_100: string;
  online: boolean;
  online_mobile?: boolean;
};

export const initRatingUpdating = async () => {
  cron.schedule("* * * * *", async () => {
    // Сортируем пользователей по их значению rating
    const sortedUsers = await Users.find()
      .sort({ rating: -1 })
      .limit(10000)
      .lean();

    /**
     * userIds - Массив пользовательских id для запроса их аватара и имени из vk api
     * top100 - Массив из топ 100 лучших пользователей (будет использоваться в последующей выдаче)
     * links - Ссылки на объекты
     * positions - Массив с позициями 10 000 людей в рейтинге, чтобы была возможность отображать позицию пользователя до 10 000-ого места
     */
    const { userIds, top100, links, positions } = sortedUsers.reduce(
      (prev, curr, index) => {
        if (index < 100) {
          const userObject: IRatingItem = {
            _id: curr._id,
            position: index + 1,
            rating: curr.rating,
            photo_100: "",
            online_status: "offline",
            name: "",
          };

          prev.top100.push(userObject);
          prev.userIds.push(curr._id);
          prev.links[curr._id] = userObject;
        }
        prev.positions.push(curr._id);

        return prev;
      },
      {
        userIds: [] as number[],
        top100: [] as IRatingItem[],
        links: {} as Record<number, IRatingItem>,
        positions: [] as number[],
      }
    );

    // Получим имена и аватары всех пользователей из api ВКонтакте
    const { data: vkUsersResponse } = await axios.get(
      `https://api.vk.com/method/users.get?access_token=${
        process.env.APP_TOKEN
      }&v=5.131&user_ids=${userIds.join(",")}&fields=photo_100,online&lang=ru`
    );

    vkUsersResponse.response.forEach((user: IVKUser) => {
      links[user.id].name = `${user.first_name} ${user.last_name}`;
      // Сохраняем онлайн статус для отображения в интерфейсе
      links[user.id].online_status = user.online
        ? user.online_mobile
          ? "mobile"
          : "online"
        : "offline";
      links[user.id].photo_100 = user.photo_100;
    });

    // Кешируем рейтинг для последующей выдачи
    const cache = JSON.stringify({
      items: top100,
      positions,
    });
    await redis.set("rating", cache);

    console.log("[Rating updated]", cache);
  });
};
```
