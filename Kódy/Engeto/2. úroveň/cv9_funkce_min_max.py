#Tvým úkolem je vytvořit dvě funkce:
# Funkce my_min(), která imituje built-in funkci min(). Funkce by měla přijmout jakoukoli sekvenci a vrátit položku s nejmenší hodnotou.


list = [31,67,12,57,89,96,34,76,98,12,80,98]


def my_min(sekvence):
    min = sekvence[0]

    for prvek in sekvence:
        if prvek < min:
            min = prvek
    return min


#Funkce my_max(), která imituje built-in funkci max(). Funkce by měla přijmout jakoukoli sekvenci a vrátit položku s největší hodnotou.


def my_max(sekvence):
    max = sekvence[0]

    for prvek2 in sekvence:
        if prvek2 > max:
            max = prvek2

    return max




print(my_min(list))
print(my_max(list))