import{
    Accordion,
    AccordionDetails,
    AccordionSummary,
    Typography,
} from "@mui/material"
import ExpandMoreIcon  from "@mui/icons-material/ExpandMore"
import PropTypes from 'prop-types';
const MyAccordion = ({title,children})=>{
    return(
        <Accordion
        elevation={0}   // Elimina sombras predeterminadas
        sx={{
          margin:".5rem",
          borderRadius: "10px", // Aplica borderRadius al componente raíz
          overflow: "hidden",   // Asegura que el contenido respete el borde redondeado
          border: "1px solid #ddd", // Opcional: agregar un borde para resaltar el diseño
        }}
        > 
            <AccordionSummary
            sx={{backgroundColor:'white'}}
            expandIcon={ <ExpandMoreIcon sx={{color:"black"}}/>}>
                <Typography Typography variant="h6" sx={{color:"black",fontWeight:700}}>{title}</Typography>
            </AccordionSummary>
            <AccordionDetails sx={{display:'flex',flexWrap:'wrap',rowGap:"1rem",columnGap:"2rem"}}>
            {children}
            </AccordionDetails>
        </Accordion>
    )
}
MyAccordion.propTypes = {
    children: PropTypes.node.isRequired,
    title:PropTypes.node.isRequired
  };
export default MyAccordion