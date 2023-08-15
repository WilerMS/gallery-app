import { lazy, Suspense } from 'react'
import {
  BrowserRouter as Router,
  Route,
  Routes
} from 'react-router-dom'
import Header from '@components/Header'

const Home = lazy(() => import('@pages/Home'))
const Explore = lazy(() => import('@pages/Explore'))
const Profile = lazy(() => import('@pages/Profile'))
const Settings = lazy(() => import('@pages/Settings'))
const NotFound = lazy(() => import('@pages/NotFound'))

export default function App () {
  return (
    <div className='App'>
      <Router>
        <Header />
          <Suspense>
            <Routes>
                <Route key='home' path='/' element={<Home />} />
                <Route key='explore' path='/explore' element={<Explore />} />
                <Route key='profile' path='/profile/:userName' element={<Profile />} />
                <Route key='settings' path='/settings' element={<Settings />} />
                <Route key='notfound' path='*' element={<NotFound />} />
            </Routes>
          </Suspense>
      </Router>
    </div>
  )
}
