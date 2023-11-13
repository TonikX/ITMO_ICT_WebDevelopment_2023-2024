# Задание №2

Реализуем подключение пользователя к конкретной игре при его успешной авторизации.

Для реализации будем использовать комнаты из socket.io и такой метод как `socket.join`.

По хранящемуся в базе данных gameId будем создавать комнату и подключать туда игроков с помощью `socket.join(“game”+gameId)`. А далее все запросы к комнате будем отправлять с помощью `io.to(“game”+gameId)`

## Сервер (hub/routes/connect.ts):

```typescript
import { SocketDataType } from "@src/types/socketData";

import { Server, Socket } from "socket.io";
import { findUser } from "@src/utils/findUser";
import { Games } from "../controllers";
import { CardsData, CardUnits } from "@src/data/cards";
import { ObjectID } from "mongodb";
import { BEFORE_GAME_DURATION, DURATION_OF_GAME } from "@/../engine/config";
import { ICard } from "@/src/models/Users";

const isUnitType = (str: string): str is CardUnits => {
  return str in CardUnits;
};

export default async (_: Server, socket: Socket) => {
  /* Достаем информацию о пользователе полученную при прохождении авторизации, 
   а также как часть запроса при подключении **/
  const socketData = socket.data as SocketDataType;
  const userId = socketData.userID;
  const watchID = socketData.watchID;

  // Находим данные пользователя в mongoDB
  const user = await findUser(userId);

  if (user) {
    try {
      // Проверяем существует ли игра к которой хочет подключиться пользователь
      const gameID =
        user?.lobby?._id.toString() || String(new ObjectID(watchID));
      const game = await Games.findOne({
        _id: gameID,
      });

      /* Если игры не существует, отдаем сообщение о завершении игры, чтобы
      не вызвать визуальных багов на фронтенде **/
      if (!game) {
        if (watchID) {
          socket.emit("gameFinished", undefined, undefined);
        } else {
          socket.emit(
            "gameFinished",
            user.history[0].userResponse,
            user.history[0].userInfo
          );
        }
        return;
      }

      // Находим в базе данных те карты пользователя, которые он выбрал для текущей игры
      let userCards = user.cards
        .filter((item) => item.position)
        .sort(function (a, b) {
          if (!a.position || !b.position) return 0;
          return a.position - b.position;
        })
        .map((item) => {
          if (isUnitType(item.entity))
            return {
              id: CardsData[item.entity].id,
              price: CardsData[item.entity].price,
              unitClass: CardsData[item.entity].unitClass,
              unitType: CardsData[item.entity].unitType,
            };
        });

      // Заносим в socket информацию об игре и колоде для удобного взаимодействия с ними дальше по коду
      socket.data.gameID = gameID;
      socket.data.deck = userCards;

      // Подключаем пользователя к нужной нам игре
      socket.join("game" + gameID);

      // Вызываем обновление игрового движка
      game.update();

      // Отправляе пользователю данные об игре, необходимые для её корректной отрисовки
      socket.emit(
        "setGame",
        game.getInitialState(),
        userCards,
        gameID,
        game.gameCompletionTime - DURATION_OF_GAME + BEFORE_GAME_DURATION,
        Date.now()
      );
    } catch (err) {
      console.log(err);
    }
  }
};
```
