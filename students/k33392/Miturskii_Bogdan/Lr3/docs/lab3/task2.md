# Задание №2

Реализуем middleware для авторизации. Строить авторизацию будем вокруг acess_token-а генерируемого платформой мини-приложений ВКонтакте при входе пользователя в игру. Для его проверки потребуется отдельный алгоритм и секретный ключ нашего мини-приложения.

## Сервер (hub/middlewares/checkSign.ts):

```typescript
import { Response, NextFunction } from "express";
import { IGetUserIDAuthInfoRequest } from "../types/request";
import { checkSignRestApi as checkSignMiddlewareUtils } from "@src/utils/checkSignRestApi";

export const checkSignMiddleware = (
  req: IGetUserIDAuthInfoRequest,
  res: Response,
  next: NextFunction
) => {
  try {
    if (!req.headers.authorization) return;

    // С помощью алгоритма проверки подписи на основе секретного ключа проверяем подлинность сессии
    if (
      !checkSignMiddlewareUtils(decodeURIComponent(req.headers.authorization), [
        process.env.VK_SECRET_KEY || "",
        process.env.VK_SECRET_GAME_KEY || "",
      ])
    ) {
      return;
    }

    // Записывает в реквест нужные нам для дальнейшей работы на бекенде в рамках этого запроса поля
    req.userID = Number(
      req.headers.authorization?.split("vk_user_id=")[1]?.split("&")[0] ||
        req.headers.authorization?.split("viewer_id=")[1]?.split("&")[0]
    );

    req.userVkRef = req.headers.authorization
      ?.split("vk_ref=")[1]
      ?.split("&")[0];

    req.userVkPlatform = req.headers.authorization
      ?.split("vk_platform=")[1]
      ?.split("&")[0];

    req.chatID = decodeURIComponent(req.headers.authorization)
      ?.split("vk_chat_id=")[1]
      ?.split("&")[0];

    next();
  } catch (err) {
    return;
  }
};
```
