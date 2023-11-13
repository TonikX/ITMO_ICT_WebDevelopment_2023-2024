# Задание №4

Реализуем функционал для взаимодействия с игровым полем. Дадим возможность игрокам отправлять запрос для создания игрового юнита и будем передавать информацию с подтверждением для всех подключенных к лобби игроков.

## Сервер (lobby/routes/spawnUnit.ts):

```typescript
import { SocketDataType } from "@src/types/socketData";
import { Games } from "../controllers";
import { Server, Socket } from "socket.io";
import { UnitsSpawnFunctions } from "@engine/units";
import { Lobbies } from "@/src/models/Lobbies";
import { BEFORE_GAME_DURATION, DURATION_OF_GAME } from "@/../engine/config";

export default (_: Server, socket: Socket) => {
  const socketData = socket.data as SocketDataType;
  let isGameStarted = false;

  // Обрабатываем запрос spawnUnit
  socket.on(
    "spawnUnit",
    async (
      unitType: keyof typeof UnitsSpawnFunctions,
      coords?: { x?: number; y?: number }
    ) => {
      // Выполняем базовые проверки на существование игрового лобби и находим его в базе
      const userId = socketData.userID;
      const gameID = socketData.gameID;

      const lobby = await Lobbies.findOne({ _id: gameID });
      if (!lobby) return;

      if (!userId || !gameID) return;

      const gameManager = await Games.findOne({ _id: gameID });
      if (!gameManager) return;

      const gameEndedAt = gameManager.gameCompletionTime;
      if (
        DURATION_OF_GAME - (gameEndedAt - Date.now()) > BEFORE_GAME_DURATION ||
        process.env.NODE_ENV === "development"
      ) {
        isGameStarted = true;
      }
      if (process.env.INFINITY_GAME === "true") {
        isGameStarted = true;
      }

      if (isGameStarted) {
        // Передаем игровому менеджеру задачу на создание юнита
        gameManager.spawnUnit({ unitType, coords, data: socketData, socket });
      }
    }
  );
};
```

## Сервер (lobby/controllers/gameManager.ts):

```typescript
spawnUnit({
    unitType,
    coords,
    data,
    socket,
  }: {
    socket: Socket;
    unitType: keyof typeof UnitsSpawnFunctions;
    coords?: { x?: number; y?: number };
    data: SocketDataType;
  }) {
    // Проверяем что пользователь не создавал юнита в последние 50мс
    if (
      this.lastSpawn[data.userID] &&
      Date.now() - this.lastSpawn[data.userID] < 50
    )
      return;

    // Проверяем наличие у пользователя карты юнита, которого он хочет создать
    const card = data.deck.find((item) => item.unitType === unitType);
    if (!card) return;

    // Обновляем игровой движок
    this.update();
    // Получаем пользователя из движка
    const user = this.getUser(data.userID);
    if (!user) return;

    // Создаем новое событие в движке
    const newActions = this.buyUnit({
      userID: data.userID,
      coords,
      unitType,
    }) as any;

    if (!newActions) return;
    this.lastSpawn[data.userID] = Date.now();

    // Отправляем всем пользователям в лобби информацию о произошедшем действии
    io.to("game" + this._id).emit("actions", newActions);

  }
```
