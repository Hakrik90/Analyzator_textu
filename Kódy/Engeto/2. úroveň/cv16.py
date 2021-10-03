# NSD (GCD v angličtině) je zkratka pro největší společný dělitel (Greatest common divisor). Tvým úkolem je vytvořit funkci my_gcd, která spočítá NSD dvou celých čísel (integer).

def my_gcd(arg1, arg2):
    argument = 0
    if arg1 <= arg2:
        argument = arg1
    else:
        argument = arg2
        
    delitel = []

    for cislo in range(argument):
        if arg1 % (cislo + 1) == 0 and arg2 % (cislo + 1) == 0:
            delitel.append(cislo + 1)
    return max(delitel)

x = 3468
y = 324

print(my_gcd(x,y))


# alternativně a lépe podle --> Euklidův algoritmus. Lze i floatt

def my_gcd(a,b):
	while b > 1:
		remainder = a % b
		if not remainder:
			break
		a,b = b,remainder
	return b

print(my_gcd(15, 75))