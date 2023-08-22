import { configureStore } from '@reduxjs/toolkit'
import imagesSlice from '@redux/features/imagesReducer'
import filtersSlice from './features/filtersReducer'

export const store = configureStore({
  reducer: {
    images: imagesSlice,
    filters: filtersSlice
  }
})

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch
