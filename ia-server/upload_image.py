import requests

# Define la URL de tu API
url = "http://10.9.121.207:8000/upload_and_detect/"

# Abre el archivo de imagen en modo binario
file_path = "manzana_roja.jpg"  # Cambia esto a la ruta de tu archivo de imagen
with open(file_path, "rb") as img_file:
    # Prepara el archivo para enviarlo en la solicitud POST
    files = {"file": img_file}  # Usa el tipo MIME correcto (por ejemplo, "image/jpeg" o "image/png")
    
    # Realiza la solicitud POST
    response = requests.post(url, files=files)

# Verifica la respuesta
    if response.status_code == 200:
        print("Imagen subida correctamente.")
        print("Respuesta:", response.json())  # Imprime la respuesta JSON que devuelve la API
    else:
        print(f"Error al subir la imagen: {response.status_code}")
        print("Respuesta:", response.text)
