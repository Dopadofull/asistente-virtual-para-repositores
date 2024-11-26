from gtts import gTTS
import os

def asistente():    
    texto = "melki te amo"
    language = 'es-us'
    speech = gTTS(tex = texto,lang = language, slow = False )
    speech.save("texto.mp3")
    os.system("start texto.mp3")

asistente()