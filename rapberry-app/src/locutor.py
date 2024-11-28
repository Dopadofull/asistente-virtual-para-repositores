from dataclasses import dataclass
import pyttsx3


@dataclass
class Locutor:
    def enunciar_objeto(self, objeto: str):
        print("estoy hablando")
        engine = pyttsx3.init()
        engine.setProperty("rate", 20)
        volume = engine.getProperty("volume")
        print(volume)
        engine.setProperty("volume", 1.0)
        engine.say("Lime milk Pomelo")
        engine.runAndWait()

        return objeto
