# Zadané hodnoty
mesta = ("Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava")
domeny = ("gmail.com", "seznam.cz", "email.cz")
slevy = ("Olomouc", "Svitavy", "Ostrava")
ceny = (150, 200, 120, 120, 100, 180)
dvojita_cara = "=" * 35
jednoducha_cara = "-" * 35

nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
AKT_ROK = 2021


print()
print('VÍTEJTE U NAŠÍ APLIKACE DESTINATIO!')
print(dvojita_cara)
print(nabidka)
print(dvojita_cara)

cislo_destinace = int(input("Vyber číslo destinace: "))

print(jednoducha_cara)

index_destinace = cislo_destinace - 1

if cislo_destinace < 1 or cislo_destinace > 6:
    print(f"Výběr: {cislo_destinace} neexistuje! Ukončuji program!")
    quit()
else:
    destinace = mesta[index_destinace]
    print('DESTINACE: ', destinace)

print(jednoducha_cara)

if destinace in slevy:
    cena = ceny[index_destinace] * 0.75
    print(f"ZÍSKÁVÁTE 25% SLEVU! CENA:{cena} Kč" )
else:
    cena = ceny[index_destinace]
    print(f"CENA JE: {cena} Kč")

print(jednoducha_cara)

cele_jmeno = input("ZAPIŠ CELÉ JMÉNO: ")
krestni_jmeno = cele_jmeno.split()[0]

if krestni_jmeno.isalpha() == False:
    print("NEPLATNE KRESTNI JMENO! UKONCUJI")
    quit()
print(dvojita_cara)

rok_narozeni = int(input("ZAPIS ROK NAROZENI: "))

if AKT_ROK - rok_narozeni >= 18:
    print("POKRACUJI...")
else:
    print('MLADISTVIM PRISTUP ODEPREN! UKONCUJI!')
    quit()
print(dvojita_cara)

email = input('ZAPIS EMAIL: ')

if '@' not in email:
    print('NEPLATNY EMAIL! UKONCUJI...')
    quit()


if email.split('@')[1] in domeny:
    print('EMAIL V PORADKU...')
    print(dvojita_cara)
else:
    print('NEPLATNY EMAIL! UKONCUJI...')
    quit()

    
nl = '\n'

print(f"Děkuji {krestni_jmeno}, za objednávku.{nl}Destinace: {destinace}| Cena jízdného: {cena}Kč {nl}Na tvůj email {email} jsme ti poslali lístek")

print(nl)