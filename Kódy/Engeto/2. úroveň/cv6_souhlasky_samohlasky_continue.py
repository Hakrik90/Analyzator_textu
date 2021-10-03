# Napiš skript, který spočítá kolik samohlásek a souhlásek obsahuje následující string s anglickou větou:

# membership test,
# metody stringu,
# vkládání nových hodnot do slovníku,
# vnořené smyčky.

sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'
samohlasky = 'aeiouy'

pocet = {'souhlasky':0, 'samohlasky':0}


for hlaska in sentence:
    if not hlaska.isalpha():
        continue
    if hlaska.lower() in samohlasky:
        pocet['souhlasky'] += 1
    else:
        pocet['samohlasky'] += 1

print(f"Souhlásek je v textu {pocet['souhlasky']}, samohlásek je {pocet['samohlasky']}.")


