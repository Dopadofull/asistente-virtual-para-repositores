import requests

# Ruta de la imagen que deseas enviar
image_path = "./manzana.jpeg"

# URL del servidor FastAPI
url = "http://10.9.120.224:8000/upload/"

# Abre la imagen en modo binario y envíala
with open(image_path, 'rb') as img:
    files = {'file': img}
    response = requests.post(url, files=files)
    print(response.json())

# ejecutar en la terminal ej  Documentos dondetengaselcodigo.py