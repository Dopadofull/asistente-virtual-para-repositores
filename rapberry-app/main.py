# from locutor import Locutor
# from servidor import Servidor
from src.camara import Camara
from src.servidor import IA
from src.locutor import Locutor
import time

def main():

    while True:
        camara = Camara()
        foto = camara.sacar_fotos()
        servidor = IA()
        respuesta = servidor.reconocer_objetos(foto)
        locutor = Locutor()
        locutor.enunciar_objetos(respuesta)

        time.sleep(3)


if __name__ == "__main__":
    main()
