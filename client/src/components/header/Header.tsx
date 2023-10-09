import { Navbar, NavbarMenu, NavbarMenuItem } from '@nextui-org/react'
import { Link } from 'react-router-dom'
import Filters from './Filters'
import Navigation from './Navigation'
import ProfileNavMenu from './ProfileNavMenu'

export default function Header () {
  return (
    <Navbar maxWidth='full' height='90px' >
      <Navigation />
      <Filters />
      <ProfileNavMenu />

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
