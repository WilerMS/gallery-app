import { useEffect, useState } from 'react'
import { fetchImages } from '@app/services/images'
import { useAppDispatch, useAppSelector } from '@redux/hooks'
import { addImages, reset } from '@redux/features/imagesReducer'
import { type FiltersState, nextFilterPage, setFilters, resetFilters } from '@redux/features/filtersReducer'

export const useImages = () => {
  const [lastPage, setLastPage] = useState(false)
  const { images } = useAppSelector(state => state.images)
  const filters = useAppSelector(state => state.filters)

  const dispatch = useAppDispatch()

  useEffect(() => {
    return () => {
      dispatch(resetFilters())
    }
  }, [])

  useEffect(() => {
    fetchImages({ ...filters })
      .then((data) => {
        if (filters.page === 1) {
          dispatch(reset(data.images))
          setLastPage(data.lastPage)
        } else if (filters.page > 1) {
          dispatch(addImages(data.images))
          setLastPage(data.lastPage)
        }
      })
      .catch(err => console.log('Error fetching images:', err))
  }, [filters.page, filters.q])

  const fetchNextPage = () => dispatch(nextFilterPage())
  const modifyFilters = (newFilter: Partial<FiltersState>) => {
    dispatch(setFilters(newFilter))
  }

  console.log({ ...filters })

  return {
    page: filters.page,
    images,
    lastPage,
    fetchNextPage,
    modifyFilters
  }
}
