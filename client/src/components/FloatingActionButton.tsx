import { AddIcon, AddImageIcon, AddItemIcon, UploadImageIcon } from '@app/icons'
import { Dropdown, DropdownItem, DropdownMenu, DropdownTrigger } from '@nextui-org/react'
import cn from 'classnames'
import { useTheme } from 'next-themes'
import { type FC } from 'react'

type Props = Record<string, any>

const FloatingActionButton: FC<Props> = () => {
  const { theme } = useTheme()

  return (
    <div className='fixed bottom-6 right-6'>
      <Dropdown>
        <DropdownTrigger
          className={cn(
            'cursor-pointer h-16 w-16 rounded-full center shadow-2xl bg-white',
            'dark:bg-slate-800'
          )}
        >
          <div>
            <AddItemIcon width={28} height={28} color={theme === 'dark' ? '#fff' : '#1C274C'} />
          </div>
        </DropdownTrigger>
        <DropdownMenu aria-label="Profile Actions" variant="flat">
          <DropdownItem
            key="new-image"
            description="Create a new image"
            startContent={
              <AddImageIcon
                width={42}
                height={42}
                color={theme === 'dark' ? '#fff' : '#1C274C'}
              />
            }
          >
            New Image
          </DropdownItem>
          <DropdownItem
            key="upload-image"
            description="Upload a new image"
            startContent={
              <UploadImageIcon
                width={42}
                height={42}
                color={theme === 'dark' ? '#fff' : '#1C274C'}
              />
            }
          >
            Upload Image
          </DropdownItem>
          <DropdownItem
            key="upload-image"
            description="Generate an image with AI"
            startContent={<h1 className='pl-[5px] text-2xl'>AI</h1>}
          >
            Generate
          </DropdownItem>
        </DropdownMenu>
      </Dropdown>
    </div>
  )
}

export default FloatingActionButton
