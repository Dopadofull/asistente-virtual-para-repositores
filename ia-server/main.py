from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os
import cv2
from ultralytics import YOLO
import numpy as np

app = FastAPI()

# Carga del modelo YOLOv5 preentrenado (modelo más pequeño por defecto)
model = YOLO("yolov5s.pt")  # Usando el modelo YOLOv5 pequeño (puedes usar "yolov5m.pt", "yolov5l.pt", etc.)

# Ruta para subir una imagen (se guarda en el directorio "upload_images")
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

# Ruta para subir una imagen y procesarla automáticamente con la IA
@app.post("/upload/")
async def upload_image_and_detect(file: UploadFile = File(...)):
    try:
        # Definir el directorio donde se guardarán las imágenes (ya existente)
        upload_dir = "upload_images"
        
        # Verificar si el directorio existe
        if not os.path.exists(upload_dir):
            return JSONResponse(content={"message": f"El directorio {upload_dir} no existe en el servidor."}, status_code=404)

        # Guardar la imagen en el directorio
        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Leer la imagen desde el archivo guardado para la detección
        img = cv2.imread(file_path)

        # Realizar la detección con YOLO
        results = model(img)  # Detecta los objetos en la imagen

        # Extraer los resultados de detección
        detections = []
        for result in results.xyxy[0].cpu().numpy():  # Resultados de detección para la primera (y única) imagen
            xmin, ymin, xmax, ymax, conf, cls = result  # Extraemos las coordenadas, confianza y clase

            # Convertir las coordenadas a enteros
            xmin, ymin, xmax, ymax = map(int, [xmin, ymin, xmax, ymax])

            # Usar el índice de clase para obtener la etiqueta del objeto detectado
            class_label = model.names[int(cls)]

            # Guardamos la información de la detección
            detections.append({
                "class": class_label,
                "confidence": float(conf),
                "bbox": {"xmin": xmin, "ymin": ymin, "xmax": xmax, "ymax": ymax}
            })

        # Retornar los resultados de la detección
        return JSONResponse(content={"message": "Imagen procesada correctamente", "detections": detections}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"message": f"Error al procesar la imagen: {str(e)}"}, status_code=500)

# Ruta principal
@app.get("/")
def read_root():
    return {"Hola": "Mundo"}