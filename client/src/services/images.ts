import { type FetchImages } from '@app/types'
import { api } from './api'
import { API_V1_URL } from '@app/constants/env'

interface FetchImagesType {
  pageParam: number | string
  filters?: Record<string, any>
}

export const fetchImages = async ({ pageParam = 1, filters = {} }: FetchImagesType) => {
  const url = new URL(`${API_V1_URL}/images`)
  url.searchParams.append('page', `${pageParam}`)
  url.searchParams.append('limit', '15')

  Object.entries(filters).forEach(([key, value]) => {
    url.searchParams.append(key, `${value}`)
  })

  return await api<FetchImages>(url)
}
