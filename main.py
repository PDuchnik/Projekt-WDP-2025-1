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

ItemsDict = {
    "Karabin": {"Usable": 1, "Quantity": 0},
    "Siekiera": {"Usable": 0, "Quantity": 0},
    "Nóż": {"Usable": 0, "Quantity": 1},
    "Rozpałka": {"Usable": 1, "Quantity": 2},
    "Drewno": {"Usable": 0, "Quantity": 5},
    "Porcja Jedzenia": {"Usable": 1, "Quantity": 3}
}

def ListEquipment(): #funkcja wypisuje wszystkie przedmioty, które gracz aktualnie posiada
    print("Posiadane przedmioty:")
    for item in ItemsDict.keys():
        if(ItemsDict[item]["Quantity"]>0):
            print(str(ItemsDict[item]["Quantity"])+"x", item)

def ItemFunction(Item): #funkcja będzie wykonywać odpowiednią akcję zależnie od wybranego przedmiotu

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
            UseItem(0)
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