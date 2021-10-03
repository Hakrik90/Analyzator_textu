# program by měl
# vygenerovat sbírku celých čísel v rozmezí mezi start (včetně) a stop (včetně)
# vytisknout list v rozmezí čísel start - stop, která jsou dělitelná vstupem divisor
# Pokud je dělitel 0, program by měl vytisknout string Cannot divide by zero.


start = int(input('Zadej celé číslo: '))
stop = int(input('Zadej vyšší celé číslo: '))
delitel = int(input('Teď zadej dělitele (celé číslo): '))


rozsah = range(start,stop + 1)

if delitel == 0:
    print('Nulou nelze dělit!')

podily = []

for podil in rozsah:
    if podil % delitel != 0:
        continue
    podily.append(podil)

print(f"Čísla v rozsahu {start} až {stop + 1}, která jsou beze zbytku dělená {delitel}, jsou {podily}.")