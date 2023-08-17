import { useEffect, useState } from 'react'
import { fetchImages } from '@app/services/images'
import { type Image } from '@app/types'

export const useImages = () => {
  const [images, setImages] = useState<Image[]>([])
  const [page, setPage] = useState(1)
  const [lastPage, setLastPage] = useState(false)
  const [filters, setFilters] = useState({ })

  useEffect(() => {
    fetchImages({ page, limit: 20, ...filters })
      .then((data) => {
        if (page === 1) {
          setImages(data.images)
          setLastPage(data.lastPage)
        } else if (page > 1) {
          setImages(prev => [...prev, ...data.images])
          setLastPage(data.lastPage)
        }
      })
      .catch(err => console.log('Error fetching images:', err))
  }, [page, filters])

  const fetchNextPage = () => setPage(prevPage => prevPage + 1)
  const modifyFilters = (newFilter: Record<string, string | number>) => {
    setFilters({ ...filters, ...newFilter })
    setPage(1)
  }

  return {
    page,
    images,
    lastPage,
    fetchNextPage,
    modifyFilters
  }
}
