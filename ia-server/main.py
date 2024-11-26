from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse 

import shutil
import os
import torch
from PIL import Image

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Puedes cambiar 'yolov5s' por otros modelos como 'yolov5m', 'yolov5l', 'yolov5x'

app = FastAPI()

# Ruta para subir una image
@app.post("/upload/")
def upload_image(file: UploadFile = File(...)):
    try:
        # Define el directorio donde se guardarán imagenes
        upload_dir = "upload_images"
        os.makedirs(upload_dir, file.filename)

        # Define el path completo donde se almacenara la imagen
        file_path = os.path.join(upload_dir,file.filename)
     
        # guarda la imagen en el servidor
        with open(file_path,"wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return JSONResponse(content={"message": "Imagen recibida correctamente", "filename": file.filename}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"message": f"Error al recibir la imagen: {str(e)}"}, status_code=500)

# Ruta principal
@app.get("/")
def read_root():
    return{"Hola":"Mundo"}

# Ruta IA para detección de objetos
@app.post("/detect/")
async def detect_objects(file: UploadFile = File(...)):
    try:
        # Guarda la imagen recibida
        upload_dir = "upload_images"
        os.makedirs(upload_dir, exist_ok=True)  # Asegúrate de que el directorio exista

        file_path = os.path.join(upload_dir, file.filename)
        
        # Guardar la imagen en el servidor
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Cargar la imagen con PIL
        img = Image.open(file_path)

        # Realizar la detección de objetos usando YOLOv5
        results = model(img)  # La imagen es procesada por el modelo YOLOv5

        # Convertir los resultados a formato JSON
        # Utilizamos pandas para obtener los resultados en formato fácil de leer
        results_json = results.pandas().xywh[0].to_dict(orient="records")

        # Devolver los resultados de las detecciones
        return JSONResponse(content={
            "message": "Detección completada correctamente",
            "filename": file.filename,
            "detections": results_json
        }, status_code=200)

    except Exception as e:
        return JSONResponse(content={"message": f"Error al procesar la imagen: {str(e)}"}, status_code=500)

    
