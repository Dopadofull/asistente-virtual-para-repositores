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
# @app.post("/upload/")
# def upload_image(file: UploadFile = File(...)):
#     try:
#         # Define el directorio donde se guardarán las imágenes
#         upload_dir = "upload_images"
        
#         # Crea el directorio si no existe
#         os.makedirs(upload_dir, exist_ok=True)

#         # Define el path completo donde se almacenará la imagen
#         file_path = os.path.join(upload_dir, file.filename)

#         # Guarda la imagen en el servidor
#         with open(file_path, "wb") as buffer:
#             shutil.copyfileobj(file.file, buffer)

#         return JSONResponse(content={"message": "Imagen recibida correctamente", "filename": file.filename}, status_code=200)

#     except Exception as e:
#         return JSONResponse(content={"message": f"Error al recibir la imagen: {str(e)}"}, status_code=500)


@app.post("/upload_and_detect/")
async def upload_image_and_detect(file: UploadFile = File(...)):
    try:
        # Definir el directorio donde se guardarán las imágenes
        upload_dir = "upload_images"

        # Crea el directorio si no existe
        os.makedirs(upload_dir, exist_ok=True)

        # Guardar la imagen en el directorio
        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Leer la imagen desde el archivo guardado para la detección
        img = cv2.imread(file_path)

        # Verificar si la imagen fue leída correctamente
        if img is None:
            return JSONResponse(content={"message": "No se pudo leer la imagen correctamente"}, status_code=400)

        # Realizar la detección con YOLO
        results = model(img)  # Detecta los objetos en la imagen
        #print(f"img: {img}")
        #print(f"results: {results}")
        print(f"type results: {type(results[0])}")
        print(f"results: {dir(results[0])}")
        print(f"results: {results[0]}")
        print(f"boxes: {results[0].boxes}")

        names = results[0].names
        boxes = results[0].boxes
        confs = boxes.conf
        clss = boxes.cls
        xyxy = boxes.xyxy
        # Extraer los resultados de detección
        detections = []
        for i in range(len(xyxy)):
            xmin, ymin, xmax, ymax = xyxy[i]
            confidence = confs[i]
            class_idx = int(clss[i])
            # Convertir las coordenadas a enteros
            xmin, ymin, xmax, ymax = map(int, [xmin, ymin, xmax, ymax])

            # Usar el índice de clase para obtener la etiqueta del objeto detectado
            class_label = names[int(class_idx)]

            # Guardamos la información de la detección
            detections.append({
                "class": class_label,
                "confidence": float(confidence),
                "bbox": {"xmin": xmin, "ymin": ymin, "xmax": xmax, "ymax": ymax}
            })

            # Para cada detección, dibujamos la caja delimitadora sobre la imagen
            cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

        # Guardar la imagen con las detecciones sobrepuestas
        detected_image_path = os.path.join(upload_dir, f"detected_{file.filename}")
        cv2.imwrite(detected_image_path, img)

        # Retornar los resultados de la detección y la imagen procesada
        return JSONResponse(content={
            "message": "Imagen procesada correctamente",
            "detections": detections,
            "detected_image_path": detected_image_path
        }, status_code=200)
    
    except Exception as e:
        # Captura cualquier error inesperado
        return JSONResponse(content={"message": f"Hubo un error: {str(e)}"}, status_code=500)
    
# Ruta principal
@app.get("/")
def read_root():
    return {"Hola": "Mundo"}