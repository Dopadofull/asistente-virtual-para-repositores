import pyttsx3

def texto_a_voz():
    texto = "hola"
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()


texto_a_voz()