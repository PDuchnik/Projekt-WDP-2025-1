Docsy, które powinny być całkiem prostolinijne w zrozumieniu, a mogą się przydać (chociaż oczywiście możemy obejść się bez nich):

https://www.w3schools.com/python/python_classes.asp
https://docs.python.org/3/library/random.html
https://www.geeksforgeeks.org/python-match-case-statement/


Tytuł roboczy: Gra Surwiwalowa (wiem, 200IQ :3)

Gra jest wzorowana na The Long Dark, odpowiednio uproszczona i uboższa.
Gracz umieszczany jest w nieokreślonym regionie (ważne, że zimnym),
jego jedynym celem jest przetrwać jak największą liczbę dni.

Rozgrywka ma formę wybierania prostych opcji spośród podanych, które
wraz z upływem czasu skutkują modyfikacją statystyk gracza, położenia,
stanu ekwipunku...

Gracz zarządza podstawowymi statystykami, spośród których najważniejsze
jest HP - po spadnięciu do 0, gra dobiega końca.

Gracz może wybrać spośród różnych aktywności, które w danym momencie
uważa za stosowne - polowanie, przejście do innej lokacji, odpoczynek...

Może również używać przedmiotów - opatrunek, rozpalenie ogniska...

# **Instrukcja użytkowania**

Aby grę dało się uruchomić, należy postawić środowisko wirtualne w folderze
zawierającym pliki używane przez grę i zainstalować pakiety z requirements.txt.

`cd <ścieżka do plików gry>`

`python3 -m venv <wybrana nazwa środowiska>`

`source <wybrana nazwaśrodowiska>/bin/activate`

`py -m pip install -r requirements.txt`