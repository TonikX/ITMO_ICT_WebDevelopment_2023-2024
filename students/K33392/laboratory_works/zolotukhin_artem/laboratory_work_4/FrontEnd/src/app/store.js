import { configureStore } from '@reduxjs/toolkit'
import authReducer from '../features/auth/authSlice'
import animalReducer from '../features/animals/animalSlice'

export const store = configureStore({
  reducer: {
    auth: authReducer,
    animals: animalReducer,
  },
})
