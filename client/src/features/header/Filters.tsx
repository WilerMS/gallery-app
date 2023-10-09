import { useDebounce } from '@app/hooks/useDebounce'
import { useImages } from '@app/hooks/useImages'
import { SearchIcon } from '@app/icons'
import { NavbarContent } from '@nextui-org/react'
import classNames from 'classnames'
import { useTheme } from 'next-themes'
import { useState, type FC, useEffect } from 'react'

const Filters: FC = () => {
  const [query, setQuery] = useState('')

  const { theme } = useTheme()
  const { modifyFilters } = useImages()

  const debouncedText = useDebounce(query)

  useEffect(() => {
    modifyFilters({ q: debouncedText })
  }, [debouncedText])

  return (
    <NavbarContent as="div">
      <div className='w-full h-full p-6 flex justify-end items-center'>
        <div
          className={classNames(
            'search w-full h-12 2xl:w-1/2 bg-gray-50 bg-opacity-50 rounded-full overflow-hidden px-5 flex items-center border border-slate-500',
            'dark:bg-gray-800 dark:border-slate-700 dark:bg-opacity-50'
          )}
        >
          <input
            type="text"
            placeholder='Search some image'
            className='outline-none w-full h-full bg-transparent'
            onChange={e => setQuery(e.currentTarget.value)}
          />
          <SearchIcon width={24} height={24} color={theme === 'dark' ? '#fff' : '#1C274C'} />
        </div>
      </div>
    </NavbarContent>
  )
}

export default Filters
