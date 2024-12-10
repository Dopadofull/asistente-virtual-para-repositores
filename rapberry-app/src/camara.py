from dataclasses import dataclass
from pathlib import Path
import cv2
import datetime
from time import sleep



@dataclass
class Camara:
    def sacar_fotos(self) -> Path:
        carpetaConImagenesTomadas = Path("./data_fake")
        
        cap = cv2.VideoCapture(0)

        leido, frame = cap.read()


        if leido == True:
                ahora = datetime.datetime.now()
                ahoraStr = ahora.strftime("%Y_%m_%d_%H_%M_%S")
                rutAlaUltimaFotoTomada = carpetaConImagenesTomadas/ f"foto_{ahoraStr}.png"
                rutAlaUltimaFotoTomada.resolve()
                cv2.imwrite(rutAlaUltimaFotoTomada, frame)
                print("Foto tomada correctamente")

        else:
                print("Error al acceder a la cámara")
                sleep(1.5)

        return rutAlaUltimaFotoTomada