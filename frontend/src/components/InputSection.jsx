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
import { useAppContext } from "@/context/AppContext";

const InputSection = () =>{
    const appContext = useAppContext();

    const {generateStructure} = appContext; 

    const generateImage = async() =>{
      console.log("Iniciamos");
      await generateStructure();
    }

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
                <MenuItem value="model1">Opción 1</MenuItem>
                <MenuItem value="model2">Opción 2</MenuItem>
                <MenuItem value="model3">Opción 3</MenuItem>
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
              onClick={generateImage}
            >
              GENERAR
            </Button>
          </Box>
        </CardContent>
      </Card>
    )
}

export default InputSection;