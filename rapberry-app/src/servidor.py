from dataclasses import dataclass
from pathlib import Path as pl
import requests

@dataclass
class IA:  
    servidor_url = "http://10.9.120.235:8000/upload"

    def reconocer_objeto(self, foto: pl):
        # Ruta de la imagen que deseas enviar
        image_path = "./data_fake/manzanin.jpeg"

        

        # Abre la imagen en modo binario y envíala
        with open(image_path, 'rb') as img:
            files = {'file': img}
            respuesta = requests.post(self.servidor_url, files=files)
            print(respuesta.json())



            return respuesta
