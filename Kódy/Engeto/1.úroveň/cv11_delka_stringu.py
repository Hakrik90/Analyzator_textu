# Zadani slova
slovo = input('Napiš slovo jaký chceš: ')

# Zjisteni delky
print('Slovo',slovo.casefold(),'obsahuje',len(slovo),'znaků.')

delka_slova = len(slovo)

# Podminka a tisk delky slova
if delka_slova > 5:
    print(slovo.capitalize(), 'obsahuje více než 5 znaků.' )
elif delka_slova > 1:
    print(slovo.capitalize(), 'obsahuje mezi 1 a 5 znaky.' )
elif delka_slova == 1:
    print(slovo.capitalize(), 'obsahuje 1 znak.')
else:
    print('Nic jsi nezadal')