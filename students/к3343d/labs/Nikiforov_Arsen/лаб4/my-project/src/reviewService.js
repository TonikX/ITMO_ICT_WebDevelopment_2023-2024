import axios from 'axios';

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
