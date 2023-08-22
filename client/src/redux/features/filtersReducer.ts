import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

export interface FiltersState {
  q: string
  page: number
  limit: string | number
}

const initialState: FiltersState = {
  q: '',
  page: 1,
  limit: 20
}

export const filtersSlice = createSlice({
  name: 'counter',
  initialState,
  reducers: {
    setFilters: (state, action: PayloadAction<Partial<FiltersState>>) => {
      return {
        ...state,
        ...action.payload,
        page: 1
      }
    },
    resetFilters: (_state) => {
      return initialState
    },
    nextFilterPage: (state) => {
      state.page += 1
    }
  }
})

// Action creators are generated for each case reducer function
export const { setFilters, resetFilters, nextFilterPage } = filtersSlice.actions

export default filtersSlice.reducer
