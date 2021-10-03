#Tvým úkolem je vytvoři funkci my_find, která bude imitovat built-in metodu pro string .find(). Funkce bude brát 2 argumenty:
    #jakoukoli sekvenci, kterou chceme prohledat
    #položku, kterou chceme najít

#Návratová hodnota by měla být:
    #index, na kterém se položka nachází v případě, že jsme položku našli
    #-1, pokud jsme položku nenašli


def my_find(sekvence, argument):
    for index,hodnota in enumerate(sekvence):
        if hodnota == argument:
            return index
    return -1



list = [13, 'čau', 34, 1, 6, 7, 'píšťalka', 89, 'Pája', 'mikymaus']
vysledek = my_find(list, 'mikymaus')
print(vysledek)

