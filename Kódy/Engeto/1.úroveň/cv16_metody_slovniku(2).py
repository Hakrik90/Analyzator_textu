# slovniky
slovnik01 = {'jmeno': 'David', 'prijmeni': 'Novak', 'vek': 33}
slovnik02 = {'pismena': ['a', 'b', 'c', 'd'], 'cisla': [1,2,3,4,5]}
slovnik03 = {'zamestnanci': {'id01': 'Marek', 'id02': 'Matous', 'id03': 'Anna'}, 'adresy': {'id01': 'Brno', 'id02': 'Praha', 'id03': 'Praha'}}

# ziskej klice i hodnoty (slovnik01)
klice_hodnoty = slovnik01.items()

# ziskej klice (slovnik02)
klice = slovnik02.keys()

# ziskej hodnoty (slovnik03)
hodnoty = slovnik03.values()

# VYZVA
# ziskej hodnoty z vnitrniho slovniku zamestnanci (slovnik03)
vyzva = slovnik03['zamestnanci'].values()


# vypiš obsah proměnných
print(klice_hodnoty)
print(klice)
print(hodnoty)
print(vyzva)
