import { type Image } from '@app/types'
import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

export interface ImageState {
  images: Image[]
}

const initialState: ImageState = {
  images: []
}

export const imagesSlice = createSlice({
  name: 'counter',
  initialState,
  reducers: {
    reset: (state, action: PayloadAction<Image[]>) => {
      return {
        images: action.payload
      }
    },
    addImages: (state, action: PayloadAction<Image[]>) => {
      console.log({ state: state.images })
      return {
        images: [
          ...state.images,
          ...action.payload
        ]
      }
    }
  }
})

// Action creators are generated for each case reducer function
export const { reset, addImages } = imagesSlice.actions

export default imagesSlice.reducer
