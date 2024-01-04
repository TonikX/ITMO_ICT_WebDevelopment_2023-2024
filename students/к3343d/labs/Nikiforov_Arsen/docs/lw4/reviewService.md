### reviewService.js

#### Введение
`reviewService.js` - это сервисный файл в приложении для управления отелем на Vue. Он обрабатывает взаимодействие с API отеля относительно операций с отзывами.

#### Структура кода
```javascript
/import axios from 'axios';

const API_URL = 'http://localhost:8000/hotel_api/api/reviews/';

class ReviewService {
    getAllReviews() {
        return axios.get(API_URL);
    }

    getReviewById(id) {
        return axios.get(API_URL + id + '/');
    }

    createReview(reviewData) {
        return axios.post(API_URL, reviewData);
    }

    updateReview(id, reviewData) {
        return axios.put(API_URL + id + '/', reviewData);
    }

    deleteReview(id) {
        return axios.delete(API_URL + id + '/');
    }
}

export default new ReviewService();

```

#### Методы

1. **getAllReviews**
   - **Описание**: Получение всех отзывов через API.
   - **Использование**: `reviewService.getAllReviews()`

2. **getReviewById**
   - **Описание**: Получение отзыва по его ID.
   - **Параметры**: `id` - ID отзыва.
   - **Использование**: `reviewService.getReviewById(id)`

3. **createReview**
   - **Описание**: Отправка нового отзыва в API.
   - **Параметры**: `reviewData` - данные нового отзыва.
   - **Использование**: `reviewService.createReview(reviewData)`

4. **updateReview**
   - **Описание**: Обновление существующего отзыва.
   - **Параметры**: `id` - ID отзыва, `reviewData` - обновленные данные отзыва.
   - **Использование**: `reviewService.updateReview(id, reviewData)`

5. **deleteReview**
   - **Описание**: Удаление отзыва по ID.
   - **Параметры**: `id` - ID отзыва.
   - **Использование**: `reviewService.deleteReview(id)`
