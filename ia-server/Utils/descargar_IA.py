import git

def clonar_repositorio(url, ruta_destino):
    try:
        # Clona el repositorio en la ruta destino
        git.Repo.clone_from(url, ruta_destino)
        print(f"Repositorio clonado en: {ruta_destino}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
url_repositorio = "https://github.com/usuario/repositorio.git"
ruta_destino = "/ruta/a/mi/carpeta/clonada"

clonar_repositorio(url_repositorio, ruta_destino)