import {
  Card,
  CardHeader,
  CardContent,
  Box,
  FormControl,
  Button,
  Typography,
  TextField,
  FormLabel,
  InputLabel,
  Select,
  MenuItem } from "@mui/material"

const InputSection = () =>{
    return(
        <Card 
        elevation={10}
        sx={{
          height: '100%',
          backgroundColor: ' #ffffff ' ,
          borderRadius: '4px',
          '& .MuiCardHeader-root': {
            borderBottom: '1px solid #e0e0e0'
          }
        }}
      >
        <CardHeader 
          title={<Typography variant="h6">Valores de Entrada</Typography>} 
          sx={{
            backgroundColor: '#f5f5f5'
          }}
        />
        <CardContent>
          <Box component="form" sx={{ display: 'flex', flexDirection: 'column', gap: 3 }}>
            <FormControl fullWidth
            sx={{display: 'flex',flexDirection:"row",columnGap:2,rowGap:1,flexWrap:"wrap"}}>
                    <TextField size="small" sx={{width:"10rem"}}/>
                    <TextField size="small" sx={{width:"10rem"}}/>
                    <TextField size="small" sx={{width:"10rem"}}/>
                    <TextField size="small" sx={{width:"10rem"}}/>
                    <TextField size="small" sx={{width:"10rem"}}/>
            </FormControl>
              <FormLabel>Selecciona lo que deseas generar</FormLabel>
            <FormControl>
              <InputLabel id="generation-select">Generar</InputLabel>
              <Select
              labelId="generation-select"
              label="Proceso">
                <MenuItem value={10}>Opción 1</MenuItem>
                <MenuItem value={20}>Opción 2</MenuItem>
                <MenuItem value={30}>Opción 3</MenuItem>
              </Select>
            </FormControl>
            <Button
              variant="contained"
              sx={{
                mt: 2,
                backgroundColor: '#1976d2',
                '&:hover': {
                  backgroundColor: '#1565c0'
                }
              }}
            >
              GENERAR
            </Button>
          </Box>
        </CardContent>
      </Card>
    )
}

export default InputSection;