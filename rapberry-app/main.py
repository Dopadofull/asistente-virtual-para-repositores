#from locutor import Locutor
#from servidor import Servidor
from src.camara import Camara
from src.servidor import Servidor
from src.locutor import Locutor
import pyttsx3

def main():
    engine = pyttsx3.init()
    camara = Camara()
    foto = camara.sacar_fotos()
    print(f"Foto guardada en: {foto}")
    servidor = Servidor()
    respuesta = servidor.reconocer_objeto(foto)
    locutor = Locutor()
    vos = locutor.enunciar_objeto(respuesta)
    engine.say(vos)
    engine.runAndWait()
