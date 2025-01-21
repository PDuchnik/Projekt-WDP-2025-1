
class MapLocation:
    Name: str
    Coordinates: tuple[int, int] #wspolrzedne sluzace do obliczania odleglosci miedzy lokacjami
    Loot:tuple #typy takie jak tereny zabudowane, strefa do polowania...
    Temperature:float

    def __init__(self, _name:str, _coordinates:tuple[int, int], _loot:tuple, _temperature:float):
        self.Name = _name
        self.Coordinates = _coordinates
        self.Loot = _loot
        self.Temperature = _temperature

WellingtonLoot = ("test1", "test2")
SkiResortLoot = ()
GasStationLoot = ()
WildernessLootGeneric = ()

Locations = (MapLocation("Wellington", (10,10), WellingtonLoot, 10),
             MapLocation("Ośrodek narciarski", (100,20), SkiResortLoot, 10),
             MapLocation("Stacja benzynowa", (-40, 50), GasStationLoot, 10),
             MapLocation("Kanion", (35, 100), WildernessLootGeneric, -30),
             MapLocation("Jezioro", (-35,0), WildernessLootGeneric, -15),)

