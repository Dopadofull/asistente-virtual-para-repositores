from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os

app = FastAPI()

# Ruta para subir una imagen
@app.post("/upload/")
def upload_image(file: UploadFile = File(...)):
    try:
        # Define el directorio donde se guardarán las imágenes
        upload_dir = "upload_images"
        
        # Crea el directorio si no existe
        os.makedirs(upload_dir, exist_ok=True)

        # Define el path completo donde se almacenará la imagen
        file_path = os.path.join(upload_dir, file.filename)

        # Guarda la imagen en el servidor
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return JSONResponse(content={"message": "Imagen recibida correctamente", "filename": file.filename}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"message": f"Error al recibir la imagen: {str(e)}"}, status_code=500)

# Ruta principal
@app.get("/")
def read_root():
    return {"Hola": "Mundo"}