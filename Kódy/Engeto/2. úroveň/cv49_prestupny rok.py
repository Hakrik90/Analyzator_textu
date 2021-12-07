#Přestupný rok nastává jednou za 4 léta. Ale tahle podmínka neplatí absolutně.
#Pokud je číslo roku dělitelné 100, rok není přestupný.
# Tohle ale neplatí, když je číslo roku dělitelné 400. V tomto případě rok přestupný je.

def is_leap(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

#verze bez if
# Definice fce
def is_leap2(y):
    # Vrati True nebo False v zavislosti na tom, jestli je prestupny
    return ((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0))