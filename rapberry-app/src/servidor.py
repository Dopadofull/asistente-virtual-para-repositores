from dataclasses import dataclass
from pathlib import Path as pl
import requests

@dataclass
class IA:  
    servidor_url = "http://10.236.128.4:8000/upload/"

    def reconocer_objeto(servidor_url,self, foto: pl):
        # Ruta de la imagen que deseas enviar
        image_path = "./manzana.jpeg"

        

        # Abre la imagen en modo binario y envíala
        with open(image_path, 'rb') as img:
            files = {'file': img}
            response = requests.post(servidor_url, files=files)
            print(response.json())


        def obtener_mensaje():
            try:
                respuesta = requests.get(servidor_url)
                if respuesta.status_code == 200:
                    # Si la respuesta es exitosa, obtienes el mensaje
                    mensaje = respuesta.json().get("mensaje")
                    print(f"Mensaje recibido: {mensaje}")
                else:
                    print(f"Error al obtener el mensaje: {respuesta.status_code}")
            except Exception as e:
                print(f"Hubo un error al conectar al servidor: {e}")

        if __name__ == "__main__":
            obtener_mensaje()
        


        return "es una Manzana"
