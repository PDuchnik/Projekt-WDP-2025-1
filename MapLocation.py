
class MapLocation:
    Name: str
    Coordinates: tuple[int, int] #wspolrzedne sluzace do obliczania odleglosci miedzy lokacjami
    Loot:tuple #typy takie jak tereny zabudowane, strefa do polowania...
    Temperature:float
    Fire:int
    def __init__(self, _name:str, _coordinates:tuple[int, int], _loot:tuple, _temperature:float):
        self.Name = _name
        self.Coordinates = _coordinates
        self.Loot = _loot
        self.Temperature = _temperature
        self.Fire = 0

WellingtonLoot = [0, 0.1, 0, 0, 0.1, 0.3, 0.2, 0.3, 0.05, 0.05]
SkiResortLoot = [0, 0.15, 0, 0, 0.2, 0.3, 0.3, 0.2, 0.1, 0.05]
GasStationLoot = [0.1, 0.2, 0, 0, 0.1, 0.2, 0.1, 0.3, 0.1, 0.15]
WildernessLootGeneric = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

Locations = (MapLocation("Wellington", (10,10), WellingtonLoot, 0),
             MapLocation("Ośrodek narciarski", (100,20), SkiResortLoot, 0),
             MapLocation("Stacja benzynowa", (-40, 50), GasStationLoot, 0),
             MapLocation("Kanion", (35, 100), WildernessLootGeneric, -30),
             MapLocation("Jezioro", (-35,0), WildernessLootGeneric, -15),)

