
# Metoda .get je velmi užitečná, když potřebujeme spočítat počet výskytů prvků. Abychom pochopili následující kód, musíme vědět něco o smyčce while.

barvy = ['zelena', 'modra', 'cerna', 'cervena', 'cervena', 'zluta', 'modra', 'seda', 'cerna' , 'cervena', 'zelena']
pocet_barev = {}

while barvy:
    barva = barvy.pop()

    if barva not in pocet_barev:
        pocet_barev[barva]=0

    pocet_barev[barva] = pocet_barev[barva] + 1

# alternativně

barvy = ['zelena', 'modra', 'cerna', 'cervena', 'cervena', 'zluta', 'modra', 'seda', 'cerna' , 'cervena', 'zelena']
pocet_barev = {}

while barvy:
    barva = barvy.pop()
    pocet_barev[barva] = pocet_barev.get(barva,0) + 1

    #>>> pocet_barev {'modra': 2, 'cerna': 2, 'seda': 1, 'zelena': 2, 'cervena': 3, 'zluta': 1}