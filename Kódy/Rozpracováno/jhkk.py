# vstupni hodnoty
MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
CENY = (150, 200, 120, 120, 100, 180)
ODDELOVAC = "=" * 35

# uvitani uzivatele
print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(ODDELOVAC)

# vypis nabidky
print(
"""
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
)
print(ODDELOVAC)

# vkladani udaju
cislo_lokality = int(input("VYBERTE CISLO LOKALITY: "))
jmeno = input("JMENO: ")
prijmeni = input("PRIJMENI: ")
rok_narozeni = int(input("ROK NAROZENI: "))
email = input("EMAIL: ")
heslo = input("HESLO: ")
print(ODDELOVAC)

# uprava zadanych hodnot
destinace = MESTA[cislo_lokality - 1]
cena = CENY[cislo_lokality - 1]

# vypisovani vystupu
print("LISTEK DO:", destinace, "CENA:", cena)
print("DEKUJI,", jmeno, "NA MAIL", email, "TI PRIJDE KRATKY DOTAZNIK")

