# Задание №3

Реализуем подключение к серверу на клиенте, а также повесим обработчики на ключевые события игры.

## Клиент (pages/Game.ts):

```typescript
/* Подключаемся по полученному с сервера lobby url, передавая параметры авторизации и watchId,
     если хотим зайти в режим наблюдателя **/
const socket = io(lobby?.url || meta?.url, {
  transports: ["websocket"],
  auth: { params: getAuthParams(), watchId: meta?.watchId },
});

// Добавляем логирование для отслеживание состояния подключения
socket.on("reconnect", () => {
  console.log("reconnect");
});

socket.on("connect", () => {
  console.log("connect");
});

// Подписываем на событие завершения игры
socket.on("gameFinished", (data, userUpdated) => {
  // Записываем в redux обновленные данные пользователя
  if (userUpdated) {
    dispatch(setUser(userUpdated));
  }
  // Разблокируем навигацию
  unblock();

  // Воспроизводим звук завршения игры
  gameEndSound.play();
  gameEndSound.on("end", () => {
    backgroundSound?.current?.play();
  });

  // Открываем страницу завершения игры, передавая данные с результатами
  replace("/game?blackScreenPopout=endGame", { ...data });
});

// Подписываемся на событие инициализации игры
socket.on("setGame", (data, deck, gameID, gameStartedAt, timeNow) => {
  console.log("setGame");

  /* ...Код для работы с визуальной составляющей (отрисовки игры)... */

  // Подписка на события внутриигрового цикла с их передачей внутрь движка игры
  socket.on("actions", (data: actionType[]) => {
    AppEngine?.insertActions(data);
  });

  /** Калибруем игровой движок в зависимости от пинга */
  socket.on("ping", (time) => {
    if (!AppEngine) return;
    AppEngine.setTimeNow(time);
  });
});
```
