import {
  BrowserRouter as Router,
  Route,
  Routes
} from 'react-router-dom'
import Home from './pages/Home'
import NotFound from './pages/NotFound'

export default function App () {
  return (
    <div className='App'>
      <Router>
        <Routes>
          <Route path='/' element={<Home />} />
          <Route path='*' element={<NotFound />} />
        </Routes>
      </Router>
    </div>
  )
}
