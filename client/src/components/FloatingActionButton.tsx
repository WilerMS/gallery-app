import { AddImageIcon, UploadImageIcon } from '@app/icons'
import { Dropdown, DropdownItem, DropdownMenu } from '@nextui-org/react'
import { useTheme } from 'next-themes'
import { type FC } from 'react'
import { Fab } from '@components/lib'

type Props = Record<string, any>

const FloatingActionDropdown: FC<Props> = () => {
  const { theme } = useTheme()

  return (
    <div className='fixed bottom-6 right-6'>
      <Dropdown>
        <Fab />
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
            key="generate-image"
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

export default FloatingActionDropdown
