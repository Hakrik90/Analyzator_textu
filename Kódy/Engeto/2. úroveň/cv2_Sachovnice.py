####Napiš program, který vytiskne šachovnici daných rozměrů.


# Zadej rozměry šachovnice
size = 10
# Zadej symboly
symbols = ['#', ' ']
# Vytvoř šachovnici
desk = []

# Doplň smyčky for, které by měly postupně nahrát celou šachovnici do proměnné 'desk'

for radek in range(size):
    linka = []

    for bunka in range(size):
        i = (radek + bunka) % len(symbols)
        linka.append(symbols[i])
    
    desk.append(''.join(linka))

# Vytiskni šachovnici
print('\n'.join(desk))