from dataclasses import dataclass
@dataclass 
class Locutor:
    def enunciar_objeto(objeto: str):
        print(f"el objeto reconocido {objeto}")
        return objeto
    
