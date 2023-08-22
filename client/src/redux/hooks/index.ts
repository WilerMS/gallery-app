import { useSelector, type TypedUseSelectorHook, useDispatch } from 'react-redux'
import { type AppDispatch, type RootState } from '../store'

export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector
export const useAppDispatch = () => useDispatch<AppDispatch>()
