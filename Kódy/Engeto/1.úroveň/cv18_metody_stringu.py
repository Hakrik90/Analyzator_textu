
muj_string = 'Abc@abc.cz a Matous@1234.cz jsou naše emailové adresy'

# do proměnné rozdeleny_string ulož muj_string jako list rozdělený podle mezer.
rozdeleny_string = muj_string.split()
print(rozdeleny_string)

# do proměnné emaily přidej pouze emailové adresy pomocí jejich indexu v proměnné rozdeleny_string.
emaily = (rozdeleny_string[0], rozdeleny_string[2])     #emaily = list()  --> emaily.append(rozdeleny_string[0])  --> emaily.append(rozdeleny_string[2])
emaily = list(emaily)
print(emaily)


# získej pouze domény (text za znakem '@') z emailů v listu emaily. První doménu ulož do proměnné domena01 a druhou do domena02.
domena01 = emaily[0].split('@')[1]
domena02 = emaily[1].split('@')[-1]

print(domena01)
print(domena02)

# rozděl stringy v promměnných domena01 a domena02 podle znaku '.' a ulož pouze první prvek (na indexu 0) do stejné proměnné.
domena01 = domena01.split('.')[0]
domena02 = domena02.split('.')[0]

print(domena01)
print(domena02)



# ověř pomocí podmínky if, zda proměnná domena01 neobsahuje žádná čísla.

bez_cisel = ''

if domena01.isalpha():
    bez_cisel = bez_cisel.join(domena01)
    print('Doména', domena01, 'byla přidána.')
else:
    print('Doména', domena01, 'nebyla přidána, protože obsahuje čísla')

# Dopln podminkovy vyraz pro 'domena02'


if domena02.isalpha():
    bez_cisel = bez_cisel.join(domena02) 
    print('Doména', domena02, 'byla přidána.')
else:
    print('Doména', domena02, 'nebyla přidána, protože obsahuje čísla')


# ZDE NIC NEDOPLNUJ, jde o nasi kontrolu :)
if (len(bez_cisel) + 1) % 4 == 0:
    print('Bezva, další zkouška úspěšně za tebou. Jen tak dál!')
else:
    print('Bohužel, někde máš chybku. Pokud si nevíš rady, mrkni se dolů na řešení.')