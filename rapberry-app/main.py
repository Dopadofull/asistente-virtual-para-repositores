# from locutor import Locutor
# from servidor import Servidor
from src.camara import Camara
from src.servidor import IA
from src.locutor import Locutor


def main():
    camara = Camara()
    foto = camara.sacar_fotos()
    servidor = IA()
    respuesta = servidor.reconocer_objeto(foto)
    locutor = Locutor()
    locutor.enunciar_objeto(respuesta)


if __name__ == "__main__":
    main()
