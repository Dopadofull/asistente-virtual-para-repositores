from dataclasses import dataclass
import pyttsx3


@dataclass
class Locutor:
    def enunciar_objeto(self, objeto: str):
        print("estoy hablando")
        engine = pyttsx3.init()
        engine.setProperty("rate", 20)
        engine.say("manzana pera tomate")
        engine.runAndWait()

        return objeto
