from dataclasses import dataclass
from pathlib import Path as pl
@dataclass 
class Camara:
    def sacar_fotos(self) -> pl:
        foto = pl("../data_fake/manzanin.jpeg")
        foto.resolve()
        return foto
