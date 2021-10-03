# Prirazeni promennych
str1 = 'New York'
str2 = 'Yorkshire'

# Najde spolecne prvky
spolecne = set(str1).intersection(str2)

# Najde unikatni prvky
unikatni = set(str1).difference(str2)

# Najde nesdilene prvky
nesdilene = set(str1).symmetric_difference(str2)

# Najde vsechny prvky
vsechny = set(str1).union(str2)

# Vypis vsechno
print(spolecne)
print(unikatni)
print(nesdilene)
print(vsechny)