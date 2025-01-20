import {
    Typography,
    AppBar,
    Toolbar,
    Box
 }from "@mui/material"
import { Construction } from "@mui/icons-material";
const Header =()=>{
    return(
      <AppBar position="static" elevation={0} sx={{ backgroundColor: '#800505',boxShadow:"2px -10px 300px 10px #00000050",height:"4rem" }}>
        <Toolbar sx={{ justifyContent: 'space-between' }}>
          <Box sx={{ display: 'flex', alignItems: 'center' }}>
              <Construction sx={{mr:2}} />
            <Typography 
              variant="h4" 
              component="h1" 
              sx={{ 
                textTransform: 'uppercase',
                color: 'white'
              }}
            >
              Proyecto de construcción de edificios
            </Typography>
          </Box>
        </Toolbar>
      </AppBar>
    )
}
export default Header;