print('Čau, budeme počítat.')
cislo_1 = int(input('Zadej první číslo: '))
cislo_2 = int(input('Zadej druhý číslo: '))

operace = True

print('Teď vybereš, co chceš s těmi čísly dělat: ')


while operace == True:
    vyber = input('Vyber si operaci: \n sčítání: "sci", \n odčítání: "odc", \n násobení: "nas", \n dělení: "del": ')
    if vyber == 'sci':
        print('Výsledek součtu', cislo_1, 'a', cislo_2, 'je', cislo_1+cislo_2)
    elif vyber == 'odc':
        print('Výsledek rozdílu', cislo_1, 'mínus', cislo_2, 'je', cislo_1-cislo_2)
    elif vyber == 'nas':
        print('Výsledek součinu', cislo_1, 'krát', cislo_2, 'je', cislo_1*cislo_2)
    elif vyber == 'del':
        print('Výsledek podílu', cislo_1, 'děleno', cislo_2, 'je', cislo_1/cislo_2)
        operace = False