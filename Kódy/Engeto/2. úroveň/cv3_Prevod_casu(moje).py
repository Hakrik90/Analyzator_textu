# Získej vstup uživatele do proměnné `time`
time = input('Vlož aktální čas ve formátu hh:mm : ')
# Rozděl do listu vstup od uživatele do proměnné `hours` a `mins`.
hours,mins = time.split(':')

# Uprav proměnou `hours` tak, aby se do proměnné `adjusted_hours` místo 24 hodinového formátu (např.: 17) uložil formát anglický (např.: 5).
hours = int(hours)
mins = int(mins)

if hours > 12:
    adjusted_hours = hours - 12
else:
    adjusted_hours = hours

if mins < 0 or mins > 59:
    print('Nesprávný formát času')
    quit()


# Do proměnné `daytime` vyber odpovídající string z dvojčlenného listu ['AM', 'PM']
list = ['AM','PM']

if hours > 12 and hours < 24:
    daytime = list[1]
elif hours < 12 and hours >= 0:
    daytime = list[0]
else:
    print('Nesprávný formát času')
    quit()

# Vytiskni převedený čas.
print(f"Je právě {adjusted_hours}:{mins} {daytime}.")