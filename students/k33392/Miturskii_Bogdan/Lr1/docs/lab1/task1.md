# Задание №1

Развернем сервер socket.io на Node TS с применением авторизации с помощью секретного ключа мини-приложений ВКонтакте.

## Сервер (hub/index.ts):

```typescript
import express from "express";

import cookieParser from "cookie-parser";

import cors from "cors";
import http from "http";
import { Server } from "socket.io";
import { checkSignMiddleware } from "./src/middlewares/checkSign";
import registerSocketHandler from "./src/routes";
import { mongooseConnect } from "@src/utils/mongooseConnect";
import { createAdapter } from "@socket.io/redis-adapter";

import { Redis } from "@/src/classes";

const app = express();

// Используем express для дальнейшего создания socket io сервера
app.use(express.json());
app.use(
  cors({
    origin: "*",
    credentials: true,
  })
);
app.use(cookieParser());

// Даём возможность установить порт сервера из env
const PORT = Number(process.env.PORT) || 6000;

// Выносим доступ к ключевому io для других файлов
export let io: Server;

// Асинхронная функция запуска необходимых баз данных и socket io сервера
async function start() {
  try {
    // Подключаемся к бд redis
    const redis = new Redis();
    const subClient = redis._redis.duplicate();
    await Promise.all([redis.init(), subClient.connect()]);

    // Подключаемся к mongoDB
    await mongooseConnect();

    // Создаем http socket.io сервер
    let server = http.createServer(app);
    let options = {
      cors: {
        origin: "*",
        methods: ["GET", "POST"],
        credentials: true,
      },
    } as {};

    // Запускаем socket.io сервер
    io = new Server(server, options);
    io.adapter(createAdapter(redis._redis, subClient));

    // Назначаем первым роутом по умолчанию авторизацию
    io.use(checkSignMiddleware);

    // Назначаем различные socket.on каждому подключившемуся сокеты прошедшему авторизацию
    io.on("connection", (socket) => {
      registerSocketHandler(io, socket);
    });

    // Запуск прослушивание порта и выводим логи
    server.listen(PORT, () => {
      console.log(`[Lobby] has been started on port ${PORT}`);
    });
  } catch (e: any) {
    console.log("Lobby Error", e.message);
    process.exit(1);
  }
}

start();
```

## Сервер (hub/middlewares/checkSign.ts):

```typescript
import { ExtendedError } from "socket.io/dist/namespace";
import { Socket } from "socket.io";
import { checkSignWebSocket } from "@src/utils/checkSignWebSocket";

type NextFunction = (err?: ExtendedError) => void;

export const checkSignMiddleware = (req: Socket, next?: NextFunction) => {
  try {
    if (!req.handshake.auth?.params) return;

    // Проверяем наличие необходимых частей ключа для проверки подлинности подписи
    if (
      !checkSignWebSocket(decodeURIComponent(req.handshake.auth?.params), [
        process.env.VK_SECRET_KEY || "",
        process.env.VK_SECRET_GAME_KEY || "",
      ])
    ) {
      return;
    }

    // Парсим id пользователя в зависимости от его точки входа в приложение
    req.data.userID = Number(
      req.handshake.auth?.params?.split("vk_user_id=")[1]?.split("&")[0] ||
        req.handshake.auth?.params?.split("viewer_id=")[1]?.split("&")[0]
    );

    // Парсим id игрового лобби, которое пришел посмотреть пользователь (если он зашел в режиме наблюдателя)
    req.data.watchID = req.handshake.auth?.watchId;

    if (next) {
      next();
    }
  } catch (err) {
    return;
  }
};
```

## Сервер (hub/routes/index.ts):

```typescript
import { ServerType, SocketType } from "@src/types/socketData";

import connectRoute from "./connect";
import disconnectRoute from "./disconnect";
import spawnUnit from "./spawnUnit";
import checkEqual from "./checkEqual";
import lobbyJoin from "./lobbyJoin";
import extraSync from "./extraSync";
import updateOnline from "./updateOnline";

// Регистрируем всевозможные socket события в одном файле
export default async (io: ServerType, socket: SocketType) => {
  connectRoute(io, socket);
  spawnUnit(io, socket);
  disconnectRoute(io, socket);
  lobbyJoin(io, socket);
  if (process.env.CHECK_EGINE_EQUAL === "true") {
    checkEqual(io, socket);
  }
  extraSync(io, socket);
  updateOnline(io, socket);
};
```
