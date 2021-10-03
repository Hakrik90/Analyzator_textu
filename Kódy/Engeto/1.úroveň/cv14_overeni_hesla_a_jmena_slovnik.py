#slovník
data = {'uzivatel1': 'heslo1', 'Marek': '1234', 'Danko': 'qwert'}

#V tomto úkolu se pokusíme ověřit, jestli heslo vložené uživatelem skutečně patří k jeho účtu.

# Zeptej se na uzivatelske jmeno a heslo
jmeno = input('Jaké je tvé uživatelské jméno?: ')
heslo = input('Jaké je tvé heslo?: ')

# Podminkovy vyraz
if data.get(jmeno) == heslo:
    print('Pojď dál!')
else:
    print('Špatné heslo nebo jméno!')



