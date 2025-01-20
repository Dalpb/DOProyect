import { createRoot } from 'react-dom/client'
import './index.css'
import { AppProvider } from '@/context/AppContext.jsx'
import App from './App'
createRoot(document.getElementById('root')).render(
    <AppProvider>
      <App />
    </AppProvider>
)
