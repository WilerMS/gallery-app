import { AddItemIcon } from '@app/icons'
import { DropdownTrigger } from '@nextui-org/react'
import cn from 'classnames'
import { useTheme } from 'next-themes'
import { type FC } from 'react'

export const FloatingActionButton: FC = () => {
  const { theme } = useTheme()
  return (
    <DropdownTrigger>
      <div
        className={cn(
          'cursor-pointer h-16 w-16 rounded-full center shadow-2xl bg-white',
          'dark:bg-slate-800'
        )}
      >
        <AddItemIcon
          width={28}
          height={28}
          color={theme === 'dark' ? '#fff' : '#1C274C'}
        />
      </div>
    </DropdownTrigger>
  )
}
