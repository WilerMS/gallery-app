import {
  BrowserRouter as Router,
  Route,
  Routes
} from 'react-router-dom'
import Home from '@pages/Home'
import NotFound from '@pages/NotFound'
import Explore from '@pages/Explore'
import Header from '@components/Header'

export default function App () {
  return (
    <div className='App'>
      <Router>
        <Header />
        <Routes>
          <Route key='home' path='/' element={<Home />} />
          <Route key='explore' path='/explore' element={<Explore />} />
          <Route key='notfound' path='*' element={<NotFound />} />
        </Routes>
      </Router>
    </div>
  )
}
