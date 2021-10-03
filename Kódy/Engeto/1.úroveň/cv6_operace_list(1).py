# Výsledky z minulé úlohy
kandidati = ['Bruno', 'Anežka']
zamestnanci = ['František', 'Bruno', 'Anna', 'Jakub', 'Klára']

# Odstraneni jmena z kandidati
kandidati.remove('Bruno')

# Tisk zbylych kandidatu
print('Bruno odstraněn z kandidati:', kandidati)

# Opakovani prvku
kandidati = kandidati * 3

# Tisk opakovani prvku v listu kandidati
print('Opakování prvku Anežka v kandidati:',kandidati)

# Spojeni listu
zamestnanci = zamestnanci + kandidati

# Tisk spojenych listu
print('Spojeni kandidati a zamestnanci: ', zamestnanci)

# Index 2
print('Na indexu 2 je: ', zamestnanci[2])

# Zjisteni posledniho indexu a prirazeni do promenne
posledni_index = len(zamestnanci) - 1

# Posledni index
print('Na', str(posledni_index) + '.', 'indexu je: ', zamestnanci[-1])