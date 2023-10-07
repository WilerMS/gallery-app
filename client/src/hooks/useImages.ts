import { useEffect, useState } from 'react'
import { fetchImages } from '@app/services/images'
import { useAppDispatch, useAppSelector } from '@redux/hooks'
import { type FiltersState, nextFilterPage, setFilters, resetFilters } from '@redux/features/filtersReducer'
import { useInfiniteQuery } from '@tanstack/react-query'

export const useImages = () => {
  const filters = useAppSelector(state => state.filters)
  const dispatch = useAppDispatch()

  const {
    data,
    hasNextPage,
    isLoading,
    isFetchingNextPage,
    fetchNextPage
  } = useInfiniteQuery(
    ['images', filters],
    ({ pageParam }) => fetchImages({ pageParam, filters }),
    {
      getNextPageParam: last => last.lastPage ? false : last.page + 1
    }
  )

  const modifyFilters = (newFilter: Partial<FiltersState>) => {
    dispatch(setFilters(newFilter))
  }

  console.log({ ...filters })

  return {
    images: data?.pages ?? [],
    page: filters.page,
    isLoading,
    hasNextPage: Boolean(hasNextPage),
    totalImages: data?.pages.reduce((prev, curr) => prev + curr.images.length, 0) ?? 0,
    isFetchingNextPage,
    fetchNextPage,
    modifyFilters
  }
}
