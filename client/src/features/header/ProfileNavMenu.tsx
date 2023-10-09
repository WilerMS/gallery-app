import { Avatar, Dropdown, DropdownItem, DropdownMenu, DropdownTrigger, NavbarContent } from '@nextui-org/react'
import { Link } from 'react-router-dom'
import DarkModeSwitch from '../../components/DarkModeSwitch'
import { useTheme } from 'next-themes'

const ProfileNavMenu = () => {
  const { theme, setTheme } = useTheme()
  const toggleTheme = () => setTheme(theme === 'light' ? 'dark' : 'light')

  return (
    <NavbarContent as="div" className='!flex-grow-0'>

        <Dropdown placement="bottom-end">
          <DropdownTrigger>
            <Avatar
              isBordered
              as="button"
              className="transition-transform"
              color="primary"
              name="Jason Hughes"
              size="md"
              src="https://i.pravatar.cc/150?u=a042581f4e29026704d"
            />
          </DropdownTrigger>
          <DropdownMenu aria-label="Profile Actions" variant="flat">
            {/* TODO: Change this to login button if not session */}
            <DropdownItem key="profile" className="h-14 gap-2">
              <Link to='/profile'>
                <div className='flex gap-4 items-center'>
                  <Avatar
                    as="div"
                    color="secondary"
                    size="sm"
                    src="https://i.pravatar.cc/150?u=a042581f4e29026704d"
                  />
                  <div>
                    <p className="font-semibold">Signed in as</p>
                    <p className="font-semibold">wiler@example.com</p>
                  </div>
                </div>
              </Link>
            </DropdownItem>
            <DropdownItem key="settings">My Settings</DropdownItem>
            <DropdownItem onClick={toggleTheme} key="theme-mode">
              <DarkModeSwitch />
            </DropdownItem>
            <DropdownItem key="logout" color="danger">
              Log Out
            </DropdownItem>
          </DropdownMenu>
        </Dropdown>
      </NavbarContent>
  )
}

export default ProfileNavMenu
