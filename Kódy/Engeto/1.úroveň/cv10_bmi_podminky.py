# Vstupni hodnoty
jmeno = 'Martin'
vaha = 160  #kg
vyska = 2 #m

# Vypocet
bmi = vaha / vyska**2

# Vytvor promennou kategorie a prirad ji hodnoy pomoci podminek
kategorie = ''
if bmi <= 18.5:
    kategorie = 'podvýživa'
elif bmi <= 25:
    kategorie = 'zdravá váha'
elif bmi <= 30:
    kategorie = 'mírná nadváha'
elif bmi <= 40:
    kategorie = 'obezita'
else:
    kategorie = 'těžká obezita'

# Vytiskni odpoved s vysledkem
print(jmeno, 'tvoje váha je', vaha,'kg a při výšce', vyska,'m, je tvé BMI', bmi,'. Patříš tedy do kategorie ',kategorie,'.')