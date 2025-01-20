from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import StreamingResponse
from fastapi.responses import FileResponse
from utils.proyect_generation import create_model,create_model_two,create_model_tree
app = FastAPI()

app.title="OPAL Proyecto Backend"


@app.get('/')
def home():
    return "Hola mundo"

@app.get("/proyect/{id}")
def get_proyect(id :int ):
    return "Devolvi imagen de proyecto " + str(id)


@app.get('/prueba')
async def get_first_structure():
    image_stream = create_model()  # Obtiene el stream de la imagen
    return StreamingResponse(image_stream, media_type='image/png')  #

@app.get("/prueba2")
async def get_second_structure():
    image_stream = create_model_two()
    return StreamingResponse(image_stream, media_type='image/png')  #

@app.get("/prueba3")
async def get_third_str():
    image_stream = create_model_tree()
    return StreamingResponse(image_stream, media_type='image/png')  #
