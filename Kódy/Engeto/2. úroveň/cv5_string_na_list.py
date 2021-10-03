#Tvým úkolem bude napsat skript, který příjme od uživatele string s čísly, která jsou oddělena čárkou a vygeneruje list celých čísel ze zadaného stringu (datový typ integer). Program by měl následně list vypsat.

# Také budeš muset ošetřit kód tak, aby si uměl poradit se situací, kdy by součástí stringu byly mezery.


inpt = input("Zadej několik čísel (odděl je čárkou): ")
nums = inpt.split(',')
result = []


for cislo in nums:
    cislo = int(cislo.strip())
    result.append(cislo)


print(f"List vypadá následovně: {result}")

