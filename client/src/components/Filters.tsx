import { SearchIcon } from '@app/icons'
import classNames from 'classnames'
import { useTheme } from 'next-themes'
import { type FC } from 'react'

const Filters: FC = () => {
  const { theme } = useTheme()

  return (
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
        />
        <SearchIcon width={24} height={24} color={theme === 'dark' ? '#fff' : '#1C274C'} />
      </div>

    </div>
  )
}

export default Filters
