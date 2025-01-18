from MapLocation import MapLocation
from ClothingLayer import ClothingLayer
import random

ClothingValuesDict = {
    "Rekawiczki1": []
}
Layer1 = ClothingLayer("Nazwa1", 10)

MapLocationsDict = {} #slownik indeksowany po nazwach lokacji, z przypisanymi wartosciami
                      #typu MapLocation dla odpowiednich lokacji
Miasto1 = MapLocation("Miasto1", (0,0), "town", 0)
Miasto1.Name
def PassTime(): #funkcja odpowiedzialna za zwiekszanie wartosci Time
    ...         #wywolywana pod koniec funkcji odpowiedzialnych za aktywnosci - przemieszczanie,
                #spanie...
def StatsLog(): #funkcja wypisujaca statystyki gracza do konsoli
    ...
def DisplayStartScreen(): #funkcja wywolywana na poczatku programu, wypisujaca wiadomosc startowa
    ...                   #czymkolwiek by nie byla
def UseItem():
    ...

Time = 0
HP = 0
Fatigue = 0
BodyTemperature = 36.6
Hunger = 100
Thirst = 100
Weight = 0


WorldTemperature = 0
CurrentLocation = ""

DisplayStartScreen()
while(True):
    StatsLog()
    actionIndex = input()
    match actionIndex:
        case 1:
            ...
            #StatsLogs()
        case 2:
            ...
            #LogEquipment()
            UseItem()
        case 3:
            ...
            #MoveLocation()
        case 4:
            ...
            #Scavenge()
        case 5:
            ...
            #Rest()
        case _:
            pass