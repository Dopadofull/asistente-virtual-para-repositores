from camara import Camara
from servidor import Servidor 
from dataclasses import dataclass
@dataclass 
class Locutor:
    def enunciar_objeto(objeto: str):
        print(f"el objeto reconocido {objeto}")
        return objeto
    
camara = Camara()
foto = camara.sacar_fotos()

servidor = Servidor()
objeto_reconocido = servidor.reconocer_objeto(foto)

locutor = Locutor()
locutor.enunciar_objeto(objeto_reconocido)