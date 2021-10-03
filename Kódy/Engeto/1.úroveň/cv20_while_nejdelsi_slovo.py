
# Napiš program, který z listu slova vybere nejdelší slovo a vytiskne do terminálu tuple s tímto nejdelším slovem a jeho délkou.

slova = [
    'Python', 'is', 'a', 'widely', 'used',
    'high-level', 'programming', 'language',
    'for', 'general-purpose', 'programming,',
    'created', 'by', 'Guido', 'van', 'Rossum',
    'and', 'first', 'released', 'in', '1991.'
]

nejdelsi_slovo = ('', 0)

while slova:
    slovicko = slova.pop(0)    # jde i jen jako slova.pop(). tedy bez 0. Jen to jde od konce
    if len(slovicko) > nejdelsi_slovo[1]:
        nejdelsi_slovo = slovicko, len(slovicko)


    


print(nejdelsi_slovo)
        

