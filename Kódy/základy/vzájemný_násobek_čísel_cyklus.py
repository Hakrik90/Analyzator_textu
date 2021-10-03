# Mas pole o peti cislich 😉 Zobraz soucet vzajemneho nasobku techto cisel 🙂


pole = [1,2,4,8,16]
soucet = sum(pole)

soucin = []

while pole:
    cislo = pole.pop()
    soucin.append(cislo * soucet)


vysledek = sum(soucin)
   

print(vysledek)