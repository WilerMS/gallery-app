import { type Children } from '@app/types.d'
import { NavbarContent, NavbarItem, NavbarMenuToggle } from '@nextui-org/react'
import { type FC, type ComponentProps } from 'react'
import { Link, useLocation, type LinkProps } from 'react-router-dom'

interface Props extends Partial<LinkProps> {
  path: `/${string}`
  children: Children
}

const NavigationLink: FC<Props> = ({ path, children, ...props }) => {
  const location = useLocation()
  const checkActive = (path: string) => location.pathname === path

  return (
    <NavbarItem
      className='text-lg'
      isActive={checkActive(path)}
    >
      <Link {...props} to={path}>{children}</Link>
    </NavbarItem>
  )
}

const Navigation = () => {
  return (
    <NavbarContent className='!flex-grow-0 !basis-[unset]'>
      <NavbarMenuToggle className="sm:hidden" />
      <Link to='/' className="md:text-2xl bg-slate-800 text-white px-4 md:px-6 py-2 rounded-2xl mr-8">
        La gallerie d&apos;Eve
      </Link>
      <NavbarContent className='gap-6  hidden md:flex'>
        <NavigationLink path='/'>Home</NavigationLink>
        <NavigationLink path='/explore'>Explore</NavigationLink>
      </NavbarContent>
    </NavbarContent>
  )
}

export default Navigation
