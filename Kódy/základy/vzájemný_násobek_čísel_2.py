pole = [1,2,4,8,16]
souciny = []

for i in pole:
    for j in pole:
        vysledek = j*i
        souciny.append(vysledek)

vysledek = sum(souciny)


print(vysledek)

    







