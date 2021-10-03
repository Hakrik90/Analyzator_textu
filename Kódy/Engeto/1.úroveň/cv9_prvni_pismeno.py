# Vytvor list 'tyden' a uloz dny v tydnu v podobe stringu
tyden = ['pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle']

# Ziskej vyber dne od uzivatele
cislo_dne = int(input("Vyber den v týdnu podle jeho čísla (1 - pondělí):"))

# Ziskej den z listu na zaklade hodnoty ziskane od uzivatele
prvni_pismeno_dne = tyden[cislo_dne-1][0]

# Ziskej tip na prvni pismeno dne od uzivatele
tip_prvniho_pismena = input("Jaké první písmeno má tebou vybraný den?: ")

# Zjistit vysledek
vysledek = prvni_pismeno_dne == tip_prvniho_pismena

# Vytiskni vysledek
print(vysledek)