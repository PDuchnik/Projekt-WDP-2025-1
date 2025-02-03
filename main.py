
from MapLocation import Locations
from Player import DropItem
from Player import StatsDict
from Player import Inventory
from Player import InventoryLog
from Player import StatsLog
from Player import Scavenge
from Player import Rest
from Player import UseItem
from Player import LocationsLog
from Player import MoveLocation
from Player import OptionsLog
from Player import GetWeight
from Player import DiffSettings
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--diff", "-d", help="poziom trudnosci", action="store_true")
args = parser.parse_args() #standardowy parser argumentow z konsoli

if args.diff: #zmiana wartosci na podstawie wybranego poziomu trudnosci
    DiffSettings["TempThreshold"] = -5
    DiffSettings["MaxHP"] = 80


#glowna petla
while StatsDict["Zdrowie"]>0:
    StatsDict["Obciążenie"] = GetWeight()
    OptionsLog()
    actionIndex = input()
    match actionIndex:
        case '1':
            StatsLog()
        case '2':
            InventoryLog()
            try:
                itemIndex = int(input("Wybierz przedmiot")) - 1
                UseItem(itemIndex)
            except:
                pass

        case '3':
            LocationsLog()
            try:
                newLocationIndex = int(input("Wybierz lokację"))-1
                MoveLocation(newLocationIndex)
            except:
                pass

        case '4':
            if (StatsDict["Obecna Lokacja"] == Locations[3] or StatsDict["Obecna Lokacja"] == Locations[4]) and Inventory["Siekiera"].Quantity == 0:
                ...
            else:
                Scavenge()
        case '5':
            ...
            try:
                Rest(int(input("Wybierz liczbę godzin")))
            except:
                pass
        case '6':
            InventoryLog()
        case '7':
            try:
                DropItem(int(input("Wybierz przedmiot")))
            except:
                pass
        case _:
            pass
input()