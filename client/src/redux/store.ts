import { configureStore } from '@reduxjs/toolkit'
import { filtersSlice, loginSlice } from '@redux/features'

export const store = configureStore({
  reducer: {
    filters: filtersSlice,
    login: loginSlice
  }
})

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch
