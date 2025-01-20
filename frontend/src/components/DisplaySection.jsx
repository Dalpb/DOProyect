import {
    Card,
    CardContent,
    CardHeader,
    CardMedia,
    Typography
}from "@mui/material"
import { useAppContext } from "@/context/AppContext"

const DisplaySection = ()=>{
    const appContext = useAppContext();

    const {imageUrl} = appContext;

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
                <CardMedia
                component="image"
                image={imageUrl}
                sx={{
                    height:"100%",
                    objectFit:"contain"
                }}
                >

                </CardMedia>
            </CardContent>
        </Card>
    )
}

export default DisplaySection