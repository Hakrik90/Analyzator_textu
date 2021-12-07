import os



soubor = input('Zadej název souboru nebo složky: '.lower())
cesta = 'C:\\Users\\phakr\\Desktop\\Python\\' + soubor

if soubor + '.pdf' == os.path.basename('C:\\Users\\phakr\\Desktop\\Python\\pokusna_sl\\prazdne.pdf'):
    print(f"Soubor {soubor} je skutečný název existujícího souboru.")
elif os.path.isdir(cesta):
    print(f"Složka {soubor} je skutečný název existující složky.")
else:
    print('Nic takového tady není')

