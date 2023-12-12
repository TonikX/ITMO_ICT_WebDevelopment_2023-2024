# Задание №1

Реализуем на клиенте удобную функцию с помощью которой в дальнейшем будет отправлять запросы на сервер.

## Клиент (utils/request.ts):

```typescript
import axios from "axios";
import axiosRetry from "axios-retry";
import { SERVER_URL } from "@/config/constants";
import getAuthParams from "./getAuthParams";

// Автоматические попытки достучаться к апи в случае отсуствия соединения
axiosRetry(axios, {
  retries: 180,
  retryDelay: (retryCount) => {
    let retryTimeout = retryCount * 500;
    if (retryTimeout > 1500) {
      retryTimeout = 1500;
    }
    return (retryTimeout = 1500);
  },
});

// Универсальная функция запросов для на сервер
export async function request<T>({
  auth = true,
  method,
  params,
  controller,
  ignoreErrors,
}: {
  method: string;
  auth?: boolean;
  params?: { [key: string]: any };
  controller?: AbortController;
  ignoreErrors?: boolean;
}) {
  const headers: { Authorization?: string } = {};
  if (auth) {
    headers.Authorization = `${getAuthParams()}`;
  }
  const response = await axios.get<T>(`${SERVER_URL}/${method}`, {
    headers,
    params,
    signal: controller?.signal,
    validateStatus: ignoreErrors ? () => true : undefined,
  });
  return response.data;
}
```
