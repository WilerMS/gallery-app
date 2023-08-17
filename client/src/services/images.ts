import { type FetchImages } from '@app/types'
import { api } from './api'
import { API_V1_URL } from '@app/constants/env'

interface FetchImagesType {
  page: number | string
  limit: number | string
  [x: string]: string | number
}

export const fetchImages = async ({ page, limit = 10, ...params }: FetchImagesType) => {
  const url = new URL(`${API_V1_URL}/images`)
  url.searchParams.append('page', `${page}`)
  url.searchParams.append('limit', `${limit}`)

  Object.entries(params).forEach(([key, value]) => {
    url.searchParams.append(key, `${value}`)
  })

  return await api<FetchImages>(url)
}
