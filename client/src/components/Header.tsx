import { Navbar, NavbarContent, NavbarItem, Input, DropdownItem, DropdownTrigger, Dropdown, DropdownMenu, Avatar, NavbarMenu, NavbarMenuItem, NavbarMenuToggle } from '@nextui-org/react'
import { Link, useLocation } from 'react-router-dom'
import DarkModeSwitcher from './DarkModeSwitcher'
import { useTheme } from 'next-themes'
import { useState } from 'react'

export default function Header () {
  const location = useLocation()
  const { theme, setTheme } = useTheme()

  const checkActive = (path: string) => location.pathname === path
  const toggleTheme = () => setTheme(theme === 'light' ? 'dark' : 'light')
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const handleCloseMenu = () => setIsMenuOpen(false)

  return (
    <Navbar maxWidth='full' height='90px' onMenuOpenChange={setIsMenuOpen}>
      <NavbarContent>
        <NavbarMenuToggle
          aria-label={isMenuOpen ? 'Close menu' : 'Open menu'}
          className="sm:hidden"
        />
        <span className="md:text-2xl bg-slate-800 text-white px-4 md:px-6 py-2 rounded-2xl mr-8">
          La gallerie d&apos;Eve
        </span>
        <NavbarContent className='gap-6  hidden md:flex'>
          <NavbarItem className='text-lg' isActive={checkActive('/')}>
            <Link to='/'>Home</Link>
          </NavbarItem>
          <NavbarItem className='text-lg' isActive={checkActive('/explore')}>
            <Link to='/explore'>Explore</Link>
          </NavbarItem>
        </NavbarContent>
      </NavbarContent>

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
              <DarkModeSwitcher />
            </DropdownItem>
            <DropdownItem key="logout" color="danger">
              Log Out
            </DropdownItem>
          </DropdownMenu>
        </Dropdown>
      </NavbarContent>

      <NavbarMenu>
        <NavbarMenuItem>
          <Link to='/'>Home</Link>
        </NavbarMenuItem>
        <NavbarMenuItem>
          <Link to='/explore'>Explore</Link>
        </NavbarMenuItem>
      </NavbarMenu>
    </Navbar>
  )
}
