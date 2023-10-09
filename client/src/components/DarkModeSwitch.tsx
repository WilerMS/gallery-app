import { MoonIcon, SunIcon } from '@app/icons'
import { useTheme } from 'next-themes'

export default function DarkModeSwitch () {
  const { theme, setTheme } = useTheme()

  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light')
  }

  return (
    <div className='flex items-center gap-3'>
      <button onClick={toggleTheme} className='flex items-center justify-center rounded-lg bg-default-100 hover:bg-default-200 w-8 h-8'>
        {theme === 'light' ? <MoonIcon /> : <SunIcon />}
      </button>
      <p>{theme === 'light' ? 'Dark Mode' : 'Light Mode'}</p>
    </div>
  )
}
