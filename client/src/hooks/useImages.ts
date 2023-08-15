import { useEffect, useState } from 'react'
import { fetchImages } from '@app/services/images'
import { type Image } from '@app/types'

export const useImages = () => {
  const [images, setImages] = useState<Image[]>([])
  const [page, setPage] = useState(1)
  const [filters, setFilters] = useState({ })

  useEffect(() => {
    fetchImages({ page, limit: 20, ...filters })
      .then((images) => {
        if (page === 1) {
          setImages(images)
        } else if (page > 1) {
          setImages(prev => [...prev, ...images])
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
    fetchNextPage,
    modifyFilters
  }
}
