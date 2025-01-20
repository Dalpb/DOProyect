import { 
    createContext,
    useContext,
    useState,
 } from "react";
import Structure from "@/service/Structure.service";
const AppContext = createContext(null);

// eslint-disable-next-line react/prop-types
export const AppProvider = ({children})=>{
    const [imageUrl,setImageUrl] = useState("/hills_placeholder.png");
    const [isLoading,setIsLoading] = useState(false);

    const changeImage =(url) =>{
        console.log(url);
        setImageUrl(url);
    }

    const generateStructure = async () =>{
        try{
            setIsLoading(true);
            const imageResult= await Structure.createModelStructure();
            changeImage(imageResult);
        }catch(error){
            console.log("EXISTE UN ERROR",error.message);
        }
        finally{
            setIsLoading(false);
        }
    }

    const provide ={
        isLoading,
        generateStructure,
        imageUrl,
        changeImage
    }

    return (
        <AppContext.Provider value={provide}>
            {children}
        </AppContext.Provider>
    )
    
}

export const useAppContext =()=>{
    return useContext(AppContext);
}


