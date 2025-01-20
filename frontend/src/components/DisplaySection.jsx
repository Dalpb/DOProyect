import {
    Card,
    CardContent,
    CardHeader,
    CardMedia,
    Typography,
    CircularProgress,
    Container
}from "@mui/material"
import { useAppContext } from "@/context/AppContext"

const DisplaySection = ()=>{
    const appContext = useAppContext();

    const {imageUrl,isLoading} = appContext;

    return(
        <Card
        elevation={10}
        sx={{
            height: '100%',
            backgroundColor: '#fff',
            borderRadius: '4px',
            '& .MuiCardHeader-root': {
              borderBottom: '1px solid #e0e0e0'
            }
          }} >

            <CardHeader
            title={<Typography variant="h6">Display</Typography>}
            sx={{
                backgroundColor: '#f5f5f5',
                height:"2rem"
              }}
            />
            <CardContent
            sx={{
                height:"80%"
            }}>
            {

                isLoading ? 
                (
                <Container sx={{
                    height:"100%",
                    display:"flex",
                    flexDirection:"column",
                    justifyContent:"center",
                    alignItems:"center",
                    gap:"1rem",
                    }}>
                    <Typography variant="h6" color="gray">Generando la imagen espere, por favor...</Typography>
                    <CircularProgress size="5rem" />
                </Container>
                )
                :
                <CardMedia
                component="img"
                image={imageUrl}
                sx={{
                  objectFit: "contain", 
                  height: "100%", 
                  width: "100%", // Asegura que ocupe todo el ancho del contenedor
                }}
              />
            }
            </CardContent>
        </Card>
    )
}

export default DisplaySection