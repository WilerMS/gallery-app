import { type FetchImages } from '@app/types'
import { api } from './api'

interface FetchImagesType {
  page: number | string
  limit: number | string
  [x: string]: string | number
}

export const fetchImages = async ({ page, limit = 10, ...params }: FetchImagesType) => {
  const url = new URL('http://localhost:5000/api/v1/images')
  url.searchParams.append('page', `${page}`)
  url.searchParams.append('limit', `${limit}`)

  Object.entries(params).forEach(([key, value]) => {
    url.searchParams.append(key, `${value}`)
  })

  const data = await api<FetchImages>(url)
  return data.images
}
