from MapLocation import Locations
from Item import Item
import ItemFunctions as itemFuncs
import numpy
import random

StatsDict = {
    "Zdrowie": 100,
    "Zmęczenie": 120,
    "Temperatura": 0,
    "Głód": 100,
    "Pragnienie": 100,
    "Obciążenie": 0,
    "Czas": 0,
    "Obecna Lokacja": Locations[0],
    "Krwawienie": False
}
Inventory = {
    "Karabin": Item(True, False, itemFuncs.RifleFunction, 0, 5),
    "Apteczka": Item(True, False, itemFuncs.MedkitFunction, 0, 1),
    "Drewno": Item(True, False, itemFuncs.WoodFunction , 0, 2),
    "Mięso": Item(True, False, itemFuncs.MeatFunction, 0, 1),
    "MRE": Item(True, False, itemFuncs.MREFunction, 0, 0.5),
    "Czekolada": Item(True, False, itemFuncs.ChocolateFunction, 0, 0.2),
    "Syrop klonowy": Item(True, False, itemFuncs.MapleSyrupFunction, 0, 0.4),
    "Woda": Item(True, False, itemFuncs.WaterFunction, 0, 1),
    "Siekiera": Item(False, False, None, 0, 2.5),
    "Amunicja": Item(False, False, None, 0, 0.1),
    "Gotowane Mięso": Item(True, False, itemFuncs.PreppedMeatFunction, 0, 1)
}
def HPDown(value):
    """Zmniejsza zdrowie gracza o podaną wartość i sprawdza, czy gracz żyje."""
    StatsDict['Zdrowie'] -= value
    if StatsDict['Zdrowie'] <= 0:
        StatsDict['Zdrowie'] = 0
        print("Gracz zginął. Koniec gry.")
    else:
        print(f"Gracz otrzymał {value} obrażeń. Zdrowie: {StatsDict['Zdrowie']}/{StatsDict['max_health']}")

def HPUp(value):
    """Regeneruje zdrowie gracza o podaną wartość, ale nie przekracza maksymalnego zdrowia."""
    StatsDict['Zdrowie'] += value
    if StatsDict['Zdrowie'] > StatsDict['max_health']:
        StatsDict['Zdrowie'] = StatsDict['max_health']
    print(f"Gracz odzyskał {value} zdrowia. Zdrowie: {StatsDict['Zdrowie']}/{StatsDict['max_health']}")

def GetTemperature(self, ambient_temperature, clothing, is_near_fire):
    """Oblicza efektywną temperaturę otoczenia na podstawie różnych czynników."""
    protection = sum(clothing.values())
    fire_bonus = 10 if is_near_fire else 0

    effective_temperature = ambient_temperature + protection + fire_bonus
    print(f"Efektywna temperatura otoczenia: {effective_temperature}°C")

    return effective_temperature

def InventoryLog(): #funkcja wypisuje wszystkie przedmioty, które gracz aktualnie posiada
    print("Posiadane przedmioty:")
    i = 1
    for item in Inventory.keys():
        print(f"{i}. " + str(Inventory[item].Quantity)+"x", item)
        i += 1
def TimeLog(): #log czasu, sformatowany
    print("Dzień: " + str(int(numpy.floor(StatsDict["Czas"])/1440) + 1))
    print("Godzina: " + str(int(numpy.floor(StatsDict["Czas"]/60))%24) + ":" + str(int(StatsDict["Czas"])%60))
def Scavenge(): #przeszukiwanie, na podstawie obecnej lokacji
    if (StatsDict["Obecna Lokacja"] == Locations[3] or StatsDict["Obecna Lokacja"] == Locations[4]) and Inventory["Siekiera"].Quantity == 0:
        ...
    else:
        loot = random.choices(population=list(Inventory.keys()), weights=StatsDict["Obecna Lokacja"].Loot, k=2)
        for item in loot:
            Inventory[item].Quantity += 1
        InventoryLog()
        PassTime(60)
def PassTime(timeToPass:int, fatigueModifier = 1): #zwieksza czas, w minutach
    StatsDict["Czas"] += timeToPass
    if fatigueModifier > 0:
        StatsDict["Zmęczenie"] -= min(StatsDict["Zmęczenie"], (timeToPass/6) * fatigueModifier)
    else:
        StatsDict["Zmęczenie"] += min(120-StatsDict["Zmęczenie"], (timeToPass/6) * -fatigueModifier)
    for location in Locations:
        location.Fire -= timeToPass
    TimeLog()
def StatsLog(): #log statystyk do konsoli
    for stat in StatsDict:
        if type(StatsDict[stat]) == type(StatsDict["Obecna Lokacja"]):
            print(stat + ': ' + StatsDict[stat].Name)
        elif stat == "Czas":
            TimeLog()
        else:
            print(stat + ': ' + str(StatsDict[stat]))
def UseItem(itemIndex:int):
    itemName = list(Inventory.keys())[itemIndex]
    Inventory[itemName].Function(StatsDict, Inventory, PassTime)
def MoveLocation(newLocationIndex): #przemieszczenie do podanej lokacji
    if Locations[newLocationIndex] != StatsDict["Obecna Lokacja"]:
        StatsDict["Obecna Lokacja"] = Locations[newLocationIndex]
        if random.choice(range(0,4)) == 0:
            AnimalEvent()
        PassTime(60)
    else:
        ...

def Rest(hours): #odpoczynek trwajacy podana liczbe godzin
    PassTime(hours*60, -1)

def LocationsLog():
    i = 0
    for loc in Locations:
        print(f"{i+1}. {Locations[i].Name}")
        i += 1

def LogOptions():
    print("1. Pokaż statystyki")
    print("2. Użyj przedmiotu")
    print("3. Przejdź do innej lokacji")
    print("4. Przeszukaj obecną lokację")
    print("5. Odpocznij")
    print("6. Pokaż ekwipunek")
def PrintEventMessage():
    rifle = "brak"
    hatchet = "brak"
    if Inventory["Karabin"].Quantity != 0:
        rifle = ""
    if Inventory["Siekiera"].Quantity != 0:
        hatchet = ""
    print("Widzisz wilka kierującego się w twoją stronę.")
    print("Jeśli sie nie obronisz, zaatakuje cię.")
    print("Wybierz przedmiot do obrony:")
    print(f"1. Karabin ({rifle})")
    print(f"2. Siekiera ({hatchet})")
    print("3. Desperacja")
def AnimalEvent():
    PrintEventMessage()
    match input():
        case '1':
            if Inventory["Karabin"].Quantity == 0 or Inventory["Amunicja"].Quantity == 0:
                AnimalEvent()
            else:
                Inventory["Amunicja"].Quantity -= 1
                if random.choice(range(0,100)) < 15:
                    HPDown(random.choice(range(10,26)))
                    StatsDict["Krwawienie"] = random.choice([True, False])
                else:
                    ...
        case '2':
            if Inventory["Siekiera"].Quantity == 0:
                AnimalEvent()
            else:
                if random.choice(range(0,100)) < 40:
                    HPDown(random.choice(range(25,50)))
                    StatsDict["Krwawienie"] = random.choice([True, False])
                else:
                    ...
        case '3':
            if random.choice(range(0, 100)) < 70:
                HPDown(random.choice(range(40,60)))
                StatsDict["Krwawienie"] = True
            else:
                ...
        case _:
            AnimalEvent()
    