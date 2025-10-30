print("Zadanie 6")

import random

droga = random.randint(1, 1000)
spalanie = float(input("Podaj średnie spalanie (w l/100km): "))
cena = 6.5

przewidywane_zuzycie = (spalanie / 100) * droga
szacowany_koszt = przewidywane_zuzycie * cena

print(f" Wylosowana droga: {droga} km")
print(f" Przewidywane zużycie paliwa: {przewidywane_zuzycie:.2f} l")
print(f" Szacowany koszt podróży: {szacowany_koszt:.2f} zł")