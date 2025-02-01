from MapLocation import MapLocation
def WoodFunction(stats:dict, inventory:dict, PassTime):
    inventory["Drewno"].Quantity -= 1
    stats["Obecna Lokacja"].Fire += 30
    PassTime(10, 1)
def EatFunction(stats:dict, value:int):
    stats["Głód"] += min(100-stats["Głód"], value)
def MREFunction(stats:dict, inventory:dict, PassTime):
    EatFunction(stats, 85)
    inventory["MRE"].Quantity -= 1
def ChocolateFunction(stats:dict, inventory:dict, PassTime):
    EatFunction(stats, 15)
    inventory["Czekolada"].Quantity -= 1
def MeatFunction(stats:dict, inventory:dict, PassTime):
    inventory["Mięso"].Quantity -= 1
    inventory["Gotowane Mięso"] += 1
    PassTime(15, 1)
def MedkitFunction(stats:dict, inventory:dict, PassTime):
    inventory["Apteczka"].Quantity -= 1
    stats["Krwawienie"] = False
def RifleFunction(stats:dict, inventory:dict, PassTime):
    if (stats["Obecna Lokacja"].Name == "Kanion" or stats["Obecna Lokacja"].Name == "Jezioro") and inventory["Amunicja"] != 0:
        inventory["Mięso"].Quantiy += 1
        PassTime(60)
def PreppedMeatFunction(stats:dict, inventory:dict, PassTime):
    EatFunction(stats, 60)
    inventory["Gotowane mięso"].Quantity -= 1
def MapleSyrupFunction(stats:dict, inventory:dict, PassTime):
    EatFunction(stats, 35)
    inventory["Syrop klonowy"].Quantity -= 1
def WaterFunction(stats:dict, inventory:dict, PassTime):
    stats["Pragnienie"] += 40
    inventory["Woda"].Quantity -= 1