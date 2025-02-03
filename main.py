import numpy
from collections.abc import Callable
import ItemFunctions
from Item import Item
from MapLocation import MapLocation
from MapLocation import Locations
from ClothingLayer import ClothingLayer
import ItemFunctions as itemFuncs
import random
from Player import DropItem
from Player import StatsDict
from Player import Inventory
from Player import InventoryLog
from Player import StatsLog
from Player import Scavenge
from Player import PassTime
from Player import Rest
from Player import UseItem
from Player import LocationsLog
from Player import MoveLocation
from Player import LogOptions
from Player import GetWeight
from Player import DiffSettings
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--diff", "-d", help="poziom trudnosci", action="store_true")
args = parser.parse_args()

if args.diff:
    DiffSettings["TempThreshold"] = -5
    DiffSettings["MaxHP"] = 80

def ChangeTemperature():
    if(StatsDict["Temperatura"]>=(-5)):
        StatsDict["Temperatura"] = StatsDict["Temperatura"] + random.choice([0,-1,-2,-3,-4,-5])
    elif(StatsDict["Temperatura"]<(-5) and StatsDict["Temperatura"]>-20):
        StatsDict["Temperatura"] = StatsDict["Temperatura"] + random.choice([5,4,3,2,1,0,-1,-2,-3,-4,-5])
    else:
        StatsDict["Temperatura"] = StatsDict["Temperatura"] + random.choice([5,4,3,2,1,0])




def UseItem1(ItemName): #funkcja pozwala graczowi wybrać jaki z przedmiotów w ekwipunku użyć
    if(ItemName in Inventory.keys() and Inventory[ItemName]["Usable"] == 1 and Inventory[ItemName]["Quantity"] > 0):
        ...#ItemFunction(ItemName)
    elif(ItemName in Inventory.keys() and (Inventory[ItemName]["Usable"] == 0 or Inventory[ItemName]["Quantity"] < 1)):
        print("Wybranego przedmiotu nie można teraz użyć.")
        UseItem(0)
    elif(ItemName == 0):
        InventoryLog()
        ChosenItem = str(input("Wpisz nazwę przedmiotu, który chcesz użyć."))
        UseItem(ChosenItem)
    else:
        print("Wybrany przedmiot nie istnieje.")
        UseItem(0)

while StatsDict["Zdrowie"]>0:
    StatsDict["Obciążenie"] = GetWeight()
    LogOptions()
    actionIndex = input()
    match actionIndex:
        case '1':
            StatsLog()
        case '2':
            InventoryLog()
            itemIndex = int(input("Wybierz przedmiot")) - 1
            UseItem(itemIndex)
        case '3':
            LocationsLog()
            newLocationIndex = int(input("Wybierz lokację"))-1
            MoveLocation(newLocationIndex)
        case '4':
            if (StatsDict["Obecna Lokacja"] == Locations[3] or StatsDict["Obecna Lokacja"] == Locations[4]) and Inventory["Siekiera"].Quantity == 0:
                ...
            else:
                Scavenge()
        case '5':
            ...
            Rest(int(input("Wybierz liczbę godzin")))
        case '6':
            InventoryLog()
        case '7':
            DropItem(int(input("Wybierz przedmiot")))
        case _:
            pass
