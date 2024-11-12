from time import sleep 
from picamera import PiCamera 


# Crea una instancia de la cámara
camera = PiCamera()

# Establece la resolución de la cámara (opcional)
camera.resolution = (1024, 768)

# Espera un momento para que la cámara se ajuste
sleep(2)

# Toma la foto y guárdala en el archivo especificado
camera.capture('/home/luka/Documentos/fotospy/mi_foto.jpg')





