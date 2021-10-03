#Tvým úkolem bude vytvořit funkci, která imituje built-in funkci sum(). Vstup bude sekvence čísel a výstup suma těchto čísel.


def my_sum(sekvence):
    suma = 0
    for cislo in sekvence:
        suma += cislo
    return suma


list = [14,57,78,34,2,89,21]

print(my_sum(list))