from googletrans import Translator
from src.servidor import IA


class Traductor:

        def traducir_lista(self,respuesta): 
                translator = Translator()
                traducciones = [translator.translate(item, src='en', dest='es').text for item in respuesta]  # Traducir cada elemento
                print(traducciones)
                return traducciones