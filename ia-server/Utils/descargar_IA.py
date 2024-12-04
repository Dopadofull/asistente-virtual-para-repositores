import subprocess
from git import Repo
import os

def clonar_repositorio(url, ruta_destino):
    try:
        # Clona el repositorio en la ruta destino
        repo= Repo.clone_from(url, ruta_destino)
        # cloned_repo.clone(ruta_destino)
        print(f"Repositorio clonado en: {ruta_destino}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
url_repositorio = "https://github.com/pjreddie/darknet"
ruta_destino = "./repo"

clonar_repositorio(url_repositorio, ruta_destino)