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
        else:
            print(stat + ': ' + str(StatsDict[stat]))

def DisplayStartScreen(): #wyswietla informacje poczatkowe - instrukcje, lore...
    ...
def UseItem():
    ...
def MoveLocation(newLocationIndex): #przemieszczenie do podanej lokacji
    StatsDict["Obecna Lokacja"] = Locations[newLocationIndex]
    PassTime(60)

def Rest(hours): #odpoczynek trwajacy podana liczbe godzin
    PassTime(hours*60, -1)

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
            if Locations[newLocationIndex] != StatsDict["Obecna Lokacja"]:
                MoveLocation(newLocationIndex)
                print(StatsDict["Obecna Lokacja"].Name)
            else:
                ...
        case '4':
            Scavenge()
        case '5':
            ...
            hoursToRest = int(input())
            Rest(hoursToRest)
        case _:
            pass