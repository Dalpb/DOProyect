import API_BASE from "@/service/config.JS";

class Structure{
    static async createModelStructure() {
        try{
            const response = await fetch(`${API_BASE}/prueba`,{method:'GET'});
            const blob = await response.blob();
            return URL.createObjectURL(blob);
        }catch(error){
            throw new Error(`No se obtuvo la imagen: ${error.message}`);
        }
    }
}

export default Structure;