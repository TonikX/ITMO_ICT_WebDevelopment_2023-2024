# Задание №4

Реализуем функцию запрос пользовательских данных которую будем вызывать в корне проекта

## Клиент (utils/getUser.ts):

```typescript
import { UserState } from "@/reducers/user.reducer";
import { request } from "./request";

import getId from "./getId";

export default async function getUser(callback: (user: UserState) => void) {
  const userId = Number(getId());
  if (!userId) return;

  const user = await request({ auth: true, method: "user/get" });
  if (!user) return;

  callback({
    ...user,
  } as UserState);
}
```
