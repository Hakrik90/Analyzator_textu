cislo01 = int(input('Zadej nějaký číslo: '))
cislo02 = int(input('Zadej další číslo: '))

operace = input('Vyber a napiš operaci dle výběru: "sčítání", "odčítání", "násobení", "dělení": ')


if 'sčítání' in operace:
    print('Výsledek je:', cislo01 + cislo02)
elif 'odčítání' in operace:
    print('Výsledek je:', cislo01 - cislo02)
elif 'násobení' in operace:
    print('Výsledek je:', cislo01 * cislo02)
elif 'dělení' in operace:
    print('Výsledek je:', cislo01 / cislo02)
else:
    print('Špatnou operaci jsi zvolil')                     

