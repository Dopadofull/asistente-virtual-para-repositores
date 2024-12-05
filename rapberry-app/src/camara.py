from dataclasses import dataclass
from pathlib import Path as pl
import cv2


@dataclass
class Camara:
    def sacar_fotos(self) -> pl:
        foto = pl("../data_fake/manzanin.jpeg")


        cap = cv2.VideoCapture(0)

        leido, frame = cap.read()

        if leido == True:
            cv2.imwrite("foto.png", frame)
            print("Foto tomada correctamente")
        else:
            print("Error al acceder a la cámara")

            
        cap.release()


        foto.resolve()
        return foto
