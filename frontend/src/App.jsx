import "./App.css"
import {
   Grid2,
} from "@mui/material"
import Header from "@/components/Header"
import InputSection from "@/components/InputSection"
import DisplaySection from "./components/DisplaySection"
function App() {

  return (
    <>
    <Header />
    <Grid2 container spacing={2} sx={{padding:"1rem 2rem",height:"calc(100% - 4rem)",
    }}>
      <Grid2 size={4}>
        <InputSection />
      </Grid2>
      <Grid2 
      size={8}>
        <DisplaySection />
      </Grid2>
    </Grid2>
    </>
  )
}

export default App
