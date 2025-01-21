from MapLocation import MapLocation
from MapLocation import Locations
from ClothingLayer import ClothingLayer
import LocationLoots as loots
import random

StatsDict = {
    "Zdrowie": 100,
    "Zmęczenie": 0,
    "Temperatura": 0,
    "Głód": 100,
    "Pragnienie": 100,
    "Obciążenie": 0,
    "Czas": 0,
    "Obecna Lokacja": Locations[0]
}

def Scavenge(time = 1):
    ...
    print(StatsDict["Obecna Lokacja"].Loot[0])
    PassTime(60 * time)
def PassTime(timeToPass:int): #funkcja odpowiedzialna za zwiekszanie wartosci Time
    StatsDict["Czas"] += timeToPass
    ...         #wywolywana pod koniec funkcji odpowiedzialnych za aktywnosci - przemieszczanie,
                #spanie...
def StatsLog(): #funkcja wypisujaca statystyki gracza do konsoli
    for stat in StatsDict:
        if type(StatsDict[stat]) == type(StatsDict["Obecna Lokacja"]):
            print(stat + ': ' + StatsDict[stat].Name)
        else:
            print(stat + ': ' + str(StatsDict[stat]))

def DisplayStartScreen(): #funkcja wywolywana na poczatku programu, wypisujaca wiadomosc startowa
    ...                   #czymkolwiek by nie byla
def UseItem():
    ...
def MoveLocation(newLocationIndex):
    StatsDict["Obecna Lokacja"] = Locations[newLocationIndex]
    PassTime(60)

DisplayStartScreen()
while True:
    actionIndex = input()
    match actionIndex:
        case '1':
            StatsLog()
        case '2':
            ...
            #LogEquipment()
            UseItem()
        case '3':
            newLocationIndex = int(input())
            MoveLocation(newLocationIndex)
            print(StatsDict["Obecna Lokacja"].Name)
        case '4':
            timeInput = int(input())
            Scavenge(timeInput)
        case '5':
            ...
            #Rest()
        case _:
            pass