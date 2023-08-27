import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

export interface LoginStateType {
  username: string
  name: string
  avatar: string
  token: string
}

const initialState: LoginStateType = {
  username: '',
  name: '',
  avatar: '',
  token: ''
}

export const loginSlice = createSlice({
  name: 'counter',
  initialState,
  reducers: {
    saveUser: (state, action: PayloadAction<LoginStateType>) => {
      state = action.payload
    }
  }
})

// Action creators are generated for each case reducer function
export const { saveUser } = loginSlice.actions

export default loginSlice.reducer
