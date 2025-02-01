import numpy

from Player import Player
from MapLocation import MapLocation
from MapLocation import Locations
from ClothingLayer import ClothingLayer
import random

StatsDict = {
    "Zdrowie": 100,
    "Zmęczenie": 120,
    "Temperatura": 0,
    "Głód": 100,
    "Pragnienie": 100,
    "Obciążenie": 0,
    "Czas": 0,
    "Obecna Lokacja": Locations[0]
}

ItemsDict = {
    "Karabin": {"Usable": 1, "Quantity": 0},
    "Siekiera": {"Usable": 0, "Quantity": 0},
    "Nóż": {"Usable": 0, "Quantity": 1},
    "Rozpałka": {"Usable": 1, "Quantity": 2},
    "Drewno": {"Usable": 0, "Quantity": 5},
    "Porcja Jedzenia": {"Usable": 1, "Quantity": 3}
}
def ChangeTemperature():
    if(StatsDict["Temperatura"]>=(-5)):
        StatsDict["Temperatura"] = StatsDict["Temperatura"] + random.choice([0,-1,-2,-3,-4,-5])
    elif(StatsDict["Temperatura"]<(-5) and StatsDict["Temperatura"]>-20):
        StatsDict["Temperatura"] = StatsDict["Temperatura"] + random.choice([5,4,3,2,1,0,-1,-2,-3,-4,-5])
    else:
        StatsDict["Temperatura"] = StatsDict["Temperatura"] + random.choice([5,4,3,2,1,0])

def ListEquipment(): #funkcja wypisuje wszystkie przedmioty, które gracz aktualnie posiada
    print("Posiadane przedmioty:")
    for item in ItemsDict.keys():
        if(ItemsDict[item]["Quantity"]>0):
            print(str(ItemsDict[item]["Quantity"])+"x", item)

def ItemFunction(Item): #funkcja będzie wykonywać odpowiednią akcję zależnie od wybranego przedmiotu
    ...
def UseItem(ItemName): #funkcja pozwala graczowi wybrać jaki z przedmiotów w ekwipunku użyć
    if(ItemName in ItemsDict.keys() and ItemsDict[ItemName]["Usable"] == 1 and ItemsDict[ItemName]["Quantity"] > 0):
        ItemFunction(ItemName)
    elif(ItemName in ItemsDict.keys() and (ItemsDict[ItemName]["Usable"] == 0 or ItemsDict[ItemName]["Quantity"] < 1)):
        print("Wybranego przedmiotu nie można teraz użyć.")
        UseItem(0)
    elif(ItemName == 0):
        ListEquipment()
        ChosenItem = str(input("Wpisz nazwę przedmiotu, który chcesz użyć."))
        UseItem(ChosenItem)
    else:
        print("Wybrany przedmiot nie istnieje.")
        UseItem(0)

Player = Player(StatsDict)
def TimeLog(): #log czasu, sformatowany
    print("Dzień: " + str(int(numpy.floor(StatsDict["Czas"])/1440) + 1))
    print("Godzina: " + str(int(numpy.floor(StatsDict["Czas"]/60))%24) + ":" + str(int(StatsDict["Czas"])%60))
def Scavenge(): #przeszukiwanie, na podstawie obecnej lokacji

    ...
    print(StatsDict["Obecna Lokacja"].Loot[0])
    PassTime(60)
def PassTime(timeToPass:int, fatigueModifier = 1): #zwieksza czas, w minutach
    StatsDict["Czas"] += timeToPass
    if fatigueModifier > 0:
        StatsDict["Zmęczenie"] -= min(StatsDict["Zmęczenie"], (timeToPass/6) * fatigueModifier)
    else:
        StatsDict["Zmęczenie"] += min(120-StatsDict["Zmęczenie"], (timeToPass/6) * -fatigueModifier)
    TimeLog()
    ...
def StatsLog(): #log statystyk do konsoli
    for stat in StatsDict:
        if type(StatsDict[stat]) == type(StatsDict["Obecna Lokacja"]):
            print(stat + ': ' + StatsDict[stat].Name)
        elif stat == "Czas":
            TimeLog()
        else:
            print(stat + ': ' + str(StatsDict[stat]))


def DisplayStartScreen(): #wyswietla informacje poczatkowe - instrukcje, lore...
    ...
def UseItem():
    ...
def MoveLocation(newLocationIndex): #przemieszczenie do podanej lokacji
    if Locations[newLocationIndex] != StatsDict["Obecna Lokacja"]:
        StatsDict["Obecna Lokacja"] = Locations[newLocationIndex]
        PassTime(60)
    else:
        ...

def Rest(hours): #odpoczynek trwajacy podana liczbe godzin
    PassTime(hours*60, -1)

DisplayStartScreen()
while True:
    actionIndex = input()
    match actionIndex:
        case '1':
            StatsLog()
        case '2':
            UseItem(0)
        case '3':
            newLocationIndex = int(input())
            MoveLocation(newLocationIndex)
        case '4':
            Scavenge()
        case '5':
            ...
            hoursToRest = int(input())
            Rest(hoursToRest)
        case _:
            pass