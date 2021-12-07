#Jako argument vezme cestu k souboru.
#Přečte soubor.
#Zavře soubor.
#Pokud soubor existuje, vrátí list, ve kterém bude každá položka reprezentovat jeden řádek souboru.
#Pokud soubor neexistuje, funkce vrátí prázdný list a vypíše zprávu: Soubor xxx nebyl nalezen!


def ctecka_radku(cesta):
    try:
        file = open(cesta)
        content = file.read()
        file.close()
        return content.split('\n')
    except OSError:
        name = cesta.split('\/')[-1]
        print('Soubor {} nebyl nalezen!'.format(name))
        return []

print(ctecka_radku('C:\\Users\\phakr\\Desktop\\soubr.txt'))