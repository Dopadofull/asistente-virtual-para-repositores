from dataclasses import dataclass
from pathlib import Path as pl


@dataclass
class Servidor:
    def reconocer_objeto(self, foto: pl):
        return "es una Manzana"
