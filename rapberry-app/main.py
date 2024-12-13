# from locutor import Locutor
# from servidor import Servidor
from src.camara import Camara
from src.servidor import IA
from src.locutor import Locutor
from src.traductor import Traductor
import time

def main():

    while True:
        camara = Camara()
        foto = camara.sacar_fotos()
        servidor = IA()
        respuesta = servidor.reconocer_objetos(foto)
        traductor = Traductor()
        textoTR = traductor.traducir_lista(respuesta)
        locutor = Locutor()
        locutor.enunciar_objetos(textoTR)

        time.sleep(3)


if __name__ == "__main__":
    main()
