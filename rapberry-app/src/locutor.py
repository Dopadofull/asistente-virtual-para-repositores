from dataclasses import dataclass
import pyttsx3
from src.servidor import IA
import requests

@dataclass
class Locutor:

    def enunciar_objeto(self,respuesta:str):
        print("estoy hablando")
        engine = pyttsx3.init()
        engine.setProperty("rate", 20)
        volume = engine.getProperty("volume")
        print(volume)
        engine.setProperty("volume", 1.0)
        engine.say(respuesta)
        engine.runAndWait()

        
    def enunciar_objetos(self,respuestas):
        print("estoy hablando")
        engine = pyttsx3.init()
        engine.setProperty("rate", 20)
        volume = engine.getProperty("volume")
        print(volume)
        engine.setProperty("volume", 1.0)
        for respuesta in respuestas:
            engine.say(respuesta)
            engine.runAndWait()

