print("Zadanie 1A:")

zad1 = 1 + 2
print(f"1.  1 + 2 = {zad1}, Typ: {type(zad1)}")
print(" + dodawania.")


zad2 = 1 + 4.5
print(f"2.  1 + 4.5 = {zad2}, Typ: {type(zad2)}")
print(" + dodawanie, 'int' i 'float' daje wynik 'float'.")


zad3 = 3 / 2
print(f"3.  3 / 2 = {zad3}, Typ: {type(zad3)}")
print(" / Dzielenie zmienoprzecinkowe")


zad4 = 4 / 2
print(f"4.  4 / 2= {zad4}, Typ: {type(zad4)}")
print("   Przy wyniku całkowitym operator / zwraca 'float'.")


zad5 = 3 // 2
print(f"5.  3 // 2= {zad5}, Typ: {type(zad5)}")
print("Dzielenie całkowite. Zwraca część całkowitą wyniku.")


zad6 = -3 // 2
print(f"6.  -3 // 2= {zad6}, Typ: {type(zad6)}")
print("Dzielenie całkowite dla liczb ujemnych. Zaokrągla w dół do najbliższej liczby całkowitej (-1.5 -> -2).")


zad7 = 11 % 2
print(f"7.  11 % 2= {zad7}, Typ: {type(zad7)}")
print("Operator modulo. Zwraca resztę z dzielenia (11 / 2 = 5 reszty 1).")


zad8 = 2 ** 10
print(f"8.  2 ** 10= {zad8}, Typ: {type(zad8)}")
print("Potęgowanie (2 do potęgi 10).")


zad9 = 8 ** (1/3)
print(f"9.  8 ** (1/3)= {zad9}, Typ: {type(zad9)}")
print(" Potęgowanie z ułamkiem. Działa jak pierwiastek (tutaj: pierwiastek sześcienny z 8).")


print("Zadanie 1B:")

zad1b = int(3.0)
print(f"1.  Wynik: {zad1b}, Typ: {type(zad1b)}")
print("Zamienia liczbę zmiennoprzecinkową (float) 3.0 na liczbę całkowitą (int) 3, obcinając część dziesiętną.")

zad2b = float(3)
print(f"2.  Wynik: {zad2b}, Typ: {type(zad2b)}")
print("Zamienia liczbę całkowitą (int) 3 na liczbę zmiennoprzecinkową (float) 3.0, dodając część dziesiętną.")

zad3b = float("3")
print(f"3.  Wynik: {zad3b}, Typ: {type(zad3b)}")
print("Zamienia tekst (string)" "3" " na liczbę zmiennoprzecinkową (float) 3.0")

zad4b = str(12.4)
print(f"4.  Wynik: {zad4b}, Typ: {type(zad4b)}")
print("Zamienia liczbę 12.4 na tekst (string) " "12.4""")

zad5b = bool(0)
print(f"5.  Wynik: {zad5b}, Typ: {type(zad5b)}")
print("W Pythonie wartość liczbowa 0 jest traktowana jako logiczny Fałsz. Każda inna liczba jest Prawdą.")