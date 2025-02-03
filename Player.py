from MapLocation import Locations
from Item import Item
import ItemFunctions as itemFuncs
import numpy
import random

DiffSettings = {
    "TempThreshold": -7,
    "MaxHP": 100
}

StatsDict = {
    "Zdrowie": DiffSettings["MaxHP"],
    "Zmęczenie": 120,
    "Temperatura": 0,
    "Temperatura otoczenia": 0,
    "Głód": 120,
    "Pragnienie": 60,
    "Obciążenie": 0,
    "Czas": 0,
    "Obecna Lokacja": Locations[0],
    "Krwawienie": False,
    "Zbieractwo": 0,
    "Polowanie": 0,
    "Ogień": Locations[0].Fire
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
    "Gotowane Mięso": Item(True, False, itemFuncs.PreppedMeatFunction, 0, 1),
}
def GetWeight():
    res = 0
    for i in Inventory:
        res += Inventory[i].Quantity*Inventory[i].Weight
    return res
def Die():
    if StatsDict["Krwawienie"]:
        print("Zgon z powodu krwawienia")
    elif StatsDict["Temperatura"] == 0:
        print("Zgon z powodu zimna")
    elif StatsDict["Pragnienie"] == 0:
        print("Zgon z powodu pragnienia")
    elif StatsDict["Głód"] == 0:
        print("Zgon z powodu głodu")
def HPDown(value):
    """Zmniejsza zdrowie gracza o podaną wartość i sprawdza, czy gracz żyje."""
    if value >= StatsDict["Zdrowie"]:
        Die()
    StatsDict["Zdrowie"] -= value

def HPUp(value):
    """Regeneruje zdrowie gracza o podaną wartość, ale nie przekracza maksymalnego zdrowia."""
    StatsDict['Zdrowie'] += min(DiffSettings["MaxHP"] - StatsDict["Zdrowie"], value)
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
    itemNo = 1 if StatsDict["Zbieractwo"] <35 else 2
    if (StatsDict["Obecna Lokacja"] == Locations[3] or StatsDict["Obecna Lokacja"] == Locations[4]) and Inventory["Siekiera"].Quantity == 0:
        Inventory["Drewno"].Quantity += itemNo
        InventoryLog()
        PassTime(60)
    else:
        loot = random.choices(population=list(Inventory.keys()), weights=StatsDict["Obecna Lokacja"].Loot, k=itemNo)
        for item in loot:
            Inventory[item].Quantity += 1
        InventoryLog()
        PassTime(60)
    StatsDict["Zbieractwo"] += 1
def PassTime(timeToPass:int, fatigueModifier = 1): #zwieksza czas, w minutach
    if StatsDict["Głód"] > 0 and StatsDict["Pragnienie"] > 0 and StatsDict["Krwawienie"] == False and StatsDict["Temperatura"] > 0:
        HPUp(timeToPass*0.1)
    if StatsDict["Głód"] == 0: HPDown(timeToPass / 21.6)
    if StatsDict["Pragnienie"] == 0: HPDown(timeToPass / 14.4)
    if StatsDict["Temperatura"] == 0: HPDown(timeToPass/7.2)
    if StatsDict["Krwawienie"]: HPDown(timeToPass / 1.2)

    StatsDict["Głód"] -= min(StatsDict["Głód"], timeToPass/6)
    StatsDict["Pragnienie"] -= min(StatsDict["Pragnienie"], timeToPass/6)

    if StatsDict["Temperatura otoczenia"] <DiffSettings["TempThreshold"]:
        StatsDict["Temperatura"] -= min(StatsDict["Temperatura"], timeToPass/6)

    if fatigueModifier > 0:
        StatsDict["Zmęczenie"] -= min(StatsDict["Zmęczenie"], (timeToPass/6) * fatigueModifier)
    else:
        StatsDict["Zmęczenie"] += min(120-StatsDict["Zmęczenie"], (timeToPass/6) * -fatigueModifier)

    for location in Locations:
        location.Fire -= min(location.Fire, timeToPass)

    StatsDict["Czas"] += timeToPass
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
    if Inventory[itemName].Quantity != 0:
        if Inventory[itemName].IsClothing:
            Inventory[itemName.Function(itemName)]
        else:
            Inventory[itemName].Function(StatsDict, Inventory, PassTime)
    else:
        print("Nie posiadasz tego przedmiotu")
def DropItem(itemIndex:int):
    itemName = list(Inventory.keys())[itemIndex]
    Inventory[itemName].Quantity -= min(Inventory[itemName].Quantity, 1)
def MoveLocation(newLocationIndex): #przemieszczenie do podanej lokacji
    if StatsDict["Zmęczenie"] == 0:
        print("Zmęczenie nie pozwala na przemieszczanie.")
        return
    if StatsDict["Obciążenie"] > 40:
        print("Obciążenie nie pozwala na przemieszczanie.")
    if Locations[newLocationIndex] != StatsDict["Obecna Lokacja"]:
        StatsDict["Obecna Lokacja"] = Locations[newLocationIndex]
        if random.choice(range(0,4)) == 0:
            AnimalEvent()
        PassTime(60, 1.5)
        StatsDict["Ogień"] = StatsDict["Obecna Lokacja"].Fire
    else:
        print("Znajdujesz się w tej lokacji.")

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
                    print("Obrona udała się.")
        case '2':
            if Inventory["Siekiera"].Quantity == 0:
                AnimalEvent()
            else:
                if random.choice(range(0,100)) < 40:
                    HPDown(random.choice(range(25,50)))
                    StatsDict["Krwawienie"] = random.choice([True, False])
                else:
                    print("Obrona udała się.")
        case '3':
            if random.choice(range(0, 100)) < 70:
                HPDown(random.choice(range(40,60)))
                StatsDict["Krwawienie"] = True
            else:
                print("Obrona udała się.")
        case _:
            AnimalEvent()

def ChangeTemperature():
    if(StatsDict["Temperatura otoczenia"]>=(-5)):
        StatsDict["Temperatura otoczenia"] = StatsDict["Temperatura otoczenia"] + random.choice([0,-1,-2,-3,-4,-5])
    elif(StatsDict["Temperatura"]<(-5) and StatsDict["Temperatura otoczenia"]>-20):
        StatsDict["Temperatura otoczenia"] = StatsDict["Temperatura otoczenia"] + random.choice([5,4,3,2,1,0,-1,-2,-3,-4,-5])
    else:
        StatsDict["Temperatura otoczenia"] = StatsDict["Temperatura otoczenia"] + random.choice([5,4,3,2,1,0])
