import axios from 'axios';

const API_URL = 'http://localhost:8000/hotel_api/api/reviews/';

class ReviewService {
  // Получение всех отзывов
  getAllReviews() {
    return axios.get(API_URL);
  }

  // Получение отзыва по ID
  getReviewById(id) {
    return axios.get(API_URL + id + '/');
  }

  // Создание нового отзыва
  createReview(reviewData) {
    return axios.post(API_URL, reviewData);
  }

  // Обновление отзыва по ID
  updateReview(id, reviewData) {
    return axios.put(API_URL + id + '/', reviewData);
  }

  // Частичное обновление отзыва по ID
  partialUpdateReview(id, reviewData) {
    return axios.patch(API_URL + id + '/', reviewData);
  }

  // Удаление отзыва по ID
  deleteReview(id) {
    return axios.delete(API_URL + id + '/');
  }
}

export default new ReviewService();

