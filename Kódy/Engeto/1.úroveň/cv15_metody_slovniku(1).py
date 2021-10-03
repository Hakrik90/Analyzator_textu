# vytvor prazdne slovniky do slovníků
muj_slovnik = {}
novy_slovnik = dict()

# vloz klice 'jméno', 'přijmení' do 'muj_slovnik' a přidej libovolne hodnoty
muj_slovnik['jméno'] = 'Pavel'
muj_slovnik['přijmení'] = 'Hakr'

# vytvor z tuple 'muj_tuple' slovnik do slovniku 'novy_slovnik'
muj_tuple = ('věk','email')
novy_slovnik = novy_slovnik.fromkeys(muj_tuple)

# dopln muj_slovnik o novy_slovnik
muj_slovnik.update(novy_slovnik)       # jde i: muj_slovnik = (muj_slovnik | novy_slovnik)

# vypln klice 'věk' a 'mail'
muj_slovnik['věk'] = 31
muj_slovnik['email'] = 'p.hakr@seznam.cz'

print(muj_slovnik)
print(novy_slovnik)




