# Prevodni pomery
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

# Pocet jednotek, ktery ma byt preveden.
kg_pocet = 80
km_pocet = 54
l_pocet = 5

# Vypocty pro prevod.
kg_vysledek = kg_lb * kg_pocet
km_vysledek = km_mile * km_pocet
l_vysledek = l_gal * l_pocet

# Vysledne odpovedi.
print(kg_pocet, 'kilogramů je',kg_vysledek, 'liber.')
print(km_pocet, 'kilometrů je', km_vysledek, 'mil.')
print(l_pocet, 'litrů je', l_vysledek, 'galonů.' )








