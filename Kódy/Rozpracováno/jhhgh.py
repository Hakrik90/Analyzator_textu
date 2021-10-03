# vstupni hodnoty
MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
CENY = (150, 200, 120, 120, 100, 180)
ODDELOVAC = "=" * 35

# uvitani uzivatele
print()
print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(ODDELOVAC)
print("""
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
""")

# vkladani udaju
lokalita = int(input("VYBERTE CISLO LOKALITY: "))
jmeno = input("KRESTNI JMENO: ")
prijmeni = input("PRIJMENI: ")
rok_narozeni = input("ROK NAROZENI: ")
email = input("ZADEJTE EMAIL: ")
heslo = input("ZADEJTE HESLO: ")

# uprava zadanych hodnot
destinace = MESTA[lokalita - 1]
cena = CENY[lokalita - 1]

# vypisovani vystupu
print(ODDELOVAC)
print(f"LISTEK DO:{destinace}")
print(f"CENA:{cena}")
print(f"DEKUJEME,{jmeno}. NA EMAIL {email} TI PRIJDE DOTAZNIK")
