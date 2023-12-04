# Конечные Точки API

## Воины

### Получение информации о всех воинах

```http
GET /api/warriors/
```

## Профессии

### Создание новой профессии

```http
POST /api/profession/create/
```

### Получение списка всех профессий

```http
GET /api/professions/
```

## Умения

### Создание нового умения

```http
POST /api/skills/create/
```

### Получение списка всех умений

```http
GET /api/skills/
```

## Полная информация о воинах

### Получение полной информации о профессиях воинов

```http
GET /api/warriors/full-info/professions/
```

### Получение полной информации о умениях воинов

```http
GET /api/warriors/full-info/skills/
```

### Получение полной информации о воине по его ID

```http
GET /api/warriors/full-info/<int:pk>/
```

## Управление воинами

### Удаление воина по его ID

```http
DELETE /api/warriors/delete/<int:pk>/
```

### Редактирование информации о воине по его ID

```http
PUT /api/warriors/edit/<int:pk>/
```
