import { configureStore } from '@reduxjs/toolkit'
import filtersSlice from '@redux/features/filtersReducer'
import loginSlice from '@redux/features/loginSlice'

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
