#Vytvoř program, který vytiskne, kolikrát se každý objekt nachází v daném listu, tuplu, nebo stringu (u stringu chceme počet jednotlivých znaků).

seq = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]
pocet_prvku = {}

while seq:
    prvek = seq.pop()
    pocet_prvku[prvek] = pocet_prvku.get(prvek,0) + 1


print(pocet_prvku)

# alternativně ####################################
seq = [1,21,5,3,5,8,321,1,2,2,32,6,9,1,4,6,3,1,2]
counts = {}
for num in seq:
    counts[str(num)] = counts.setdefault(str(num),0) + 1
print(counts)