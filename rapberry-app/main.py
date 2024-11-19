#from locutor import Locutor
#from servidor import Servidor
from src.camara import Camara



def main():
    # Crear una instancia de la clase Camara
    camara = Camara()
    
    # Llamamos al método sacar_fotos() para simular la toma de una foto
    foto = camara.sacar_fotos()
    
    # Aquí podrías hacer algo con la foto, como mostrarla o procesarla.
    print(f"Foto guardada en: {foto}")