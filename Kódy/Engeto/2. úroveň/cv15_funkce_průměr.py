# Vytvoř funkci, která spočítá průměrnou hodnotu pro danou sekvenci číselných hodnot.

def mean(sekvence):
    suma = 0
    for cislo in sekvence:
        suma += cislo
    return suma / len(sekvence)


data = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]

print(mean(data))




#alternativně a jednodušeji

def mean2(values):
    return sum(values)/len(values)

# Nase data
data = [35, 14, 26, 48, 49, 26, 18, 25, 16, 16, 39, 17, 10, 29, 30]

# Pouziti a funkce mean a tisk vysledku
print(mean2(data))
