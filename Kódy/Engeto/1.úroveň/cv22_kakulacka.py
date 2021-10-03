# Pozdrav uživatele a umožni mu zapsat dvě vstupní proměnné
print('Ahoj, nejprve vyber dvě čísla! :)')
print()                                                             # jen mezera v textu, aby to léoe vypadalo =)
number01 = int(input('Prosím, zadejte prvni číslo: '))
number02 = int(input('Prosím, zadejte druhé číslo: '))



# Tento text nechceme opakovat, proto patří před smyčku while
print('Nyní vyber operaci, kterou chceš s čísly provést: ')
print()  


                                                                    #jenom mezera v textu =)
# Zapiš nekonečnou smyčku
# mod kalkulacky je ON
mod = True
while mod == True:
# Vypiš jaké operace může uživatel provádět a možnost zapsat input()
    choice = str(input('''
------------------------
Sčítání:    "sci",
Odčítání:   "odc",
Násobení:   "nas",
Dělení:     "del",
Ukonči:     "off",
----------------------
Vyber si operaci: '''))
    # Sem zapiš podmínky, které spojí tebou nabízené operace a následný print() výsledku
    if choice == 'sci':
        print(str(number01)+ ' + ' + str(number02) + ' = ' + str(number01 + number02))
    elif choice == 'odc':
        print(str(number01) + ' - ' + str(number02) + ' = ' + str(number01 - number02))
    elif choice == 'nas':
        print(str(number01) + ' * ' + str(number02) + ' = ' + str(number01 * number02))
    elif choice == 'del':
        print(str(number01) + ' / ' + str(number02) + ' = ' + str(number01 / number02))
    elif choice == 'off': # prepnu mod OFF
        print('Počtům zdar!')
        mod = False                                              #musíme dát false jinak by se to ptalo furt dokonala na operaci