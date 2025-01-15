from MapLocation import MapLocation
import random
Time = 0
Stats = {} #statystyki gracza bedziemy trzymac w slowniku, indeksowanym po nazwach statystyk
           #--byc moze zmienimy na osobna dataclass--
MapLocationsDict = {} #slownik indeksowany po nazwach lokacji, z przypisanymi wartosciami
                      #typu MapLocation dla odpowiednich lokacji
Miasto1 = MapLocation("Miasto1", (0,0), "town")
Miasto1.Name
def PassTime(): #funkcja odpowiedzialna za zwiekszanie wartosci Time
    ...         #wywolywana pod koniec funkcji odpowiedzialnych za aktywnosci - przemieszczanie,
                #spanie...
def StatsLog(): #funkcja wypisujaca statystyki gracza do konsoli
    ...
def StatsUpdate(statsChange:dict): #funkcja zmieniajaca wartosci statystyk;
    ...                            #dla kazdego elementu z statsChange, zmieniony zostanie element
                                   #Stats o odpowiadajacej nazwie


def DisplayStartScreen(): #funkcja wywolywana na poczatku programu, wypisujaca wiadomosc startowa
    ...                   #czymkolwiek by nie byla

DisplayStartScreen()
while(True):
    StatsLog()
    actionIndex = input()
    match actionIndex:
        case _:
            pass
    #StatsUpdate()