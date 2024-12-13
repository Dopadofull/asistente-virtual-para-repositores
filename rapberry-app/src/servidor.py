from dataclasses import dataclass
from pathlib import Path as pl
import requests

@dataclass
class IA:  
    servidor_url = "http://10.9.120.188:8000/upload_and_detect/"

    def reconocer_objetos(self, foto: pl)->str:
        # Ruta de la imagen que deseas enviar
        #image_path = "./data_fake/naranja.jpg"

        

        # Abre la imagen en modo binario y envíala
        with open(foto, 'rb') as img:
            files = {'file': img}
            respuesta = requests.post(self.servidor_url, files=files)
            print("esta es la respuesta del servidor",respuesta.json())

            objetos = list(map(lambda x: x["class"], respuesta.json()["detections"]))
            print(f"objetos detectados: {objetos}")

            return objetos
