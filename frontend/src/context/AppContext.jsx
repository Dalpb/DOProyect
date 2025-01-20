import { 
    createContext,
    useContext,
    useState,
 } from "react";

const AppContext = createContext(null);

// eslint-disable-next-line react/prop-types
export const AppProvider = ({children})=>{
    const [imageUrl,setImageUrl] = useState("/hills_placeholder.png");

    const changeImage =(url) =>{
        setImageUrl(url);
    }


    const provide ={
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


