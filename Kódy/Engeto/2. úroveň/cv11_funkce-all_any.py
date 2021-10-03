# Tvým úkolem je vytvořit 2 funkce:

# Funkce my_all(), která imituje built-in funkci all(). Funkce bude brát sekvenci a vrátí True, pokud mají všechny prvky v sekvenci boolean hodnotu True nebo pokud je sekvence prázdná. Jinak fuknce vrací False.

def my_all(sekvence):
    for prvek in sekvence:
        if not prvek:
            return False
    return True


# Funkce my_any(), která imituje built-in funkci any(). Funkce bude brát sekvenci a vrátí True, pokud má aspoň jeden prvek v sekvenci boolean hodnotu True. V opačném případě a také pokud je sekvence prázdná vrací fuknce False.


def my_any(sekvence):
    for prvek in sekvence:
        if prvek:
            return True
    return False


list = [3, 15, 12, 4, 6, []]
print(my_all(list))
print(my_any(list))