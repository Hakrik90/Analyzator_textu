# Tvým úkolem je vytvořit funkci s názvem my_reversed, která bude imitovat built-in funkci reversed(). Funkce vezme jakoukoli sekvenci jako vstup a vrátí list prvků v opačném pořadí.

def my_reversed(sekvence):
    list = []
    
    for hodnota in sekvence:
        list.insert(0,hodnota)
    return list

print(my_reversed('čágobelo magore'))

    
# nebo

def my_reversed_2(sekvence):
    return list(sekvence [::-1])

print(my_reversed_2('Lionel Messi'))
