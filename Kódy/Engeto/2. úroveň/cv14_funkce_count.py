#Vytvoř funkci, která zjišťuje počet výskytů daného prvku. Jako vstup bere prvek, který hledáme a sekvenci, ve které ho chceme najít.

#Příklad fungování funkce my_count():

names = ['Rob', 'Jim', 'Mark', 'Mark', 'Mark',
'Bob', 'Mark', 'Bob', 'Bob', 'Rob', 'Jim',
'Mark', 'Mark', 'Bob', 'Mark']


def my_count(prvek, hodnoty):
    pocet = 0
    for jmeno in hodnoty:
        if jmeno == prvek:
            pocet += 1
    return pocet

print(my_count('Bob',names))