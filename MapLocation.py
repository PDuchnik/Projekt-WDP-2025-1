from dataclasses import dataclass

@dataclass
class MapLocation:
    Name: str
    Coordinates: tuple[int, int] #wspolrzedne sluzace do obliczania odleglosci miedzy lokacjami
    Type:str #typy takie jak tereny zabudowane, strefa do polowania...

    def __init__(self, _name:str, _coordinates:tuple[int, int], _type:str):
        self.Name = _name
        self.Coordinates = _coordinates
        self.Type = _type
