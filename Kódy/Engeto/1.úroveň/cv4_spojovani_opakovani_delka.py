# Ukladani jmena
jmeno = input('Japa se menuješ? ')

# Tisk jmena
print(jmeno)

# Ukladani prijmeni
prijmeni = input('A copa je to druhý jméno za tim prvnim? ')

# Tisk prijmeni
print(prijmeni)

# Vytvoreni a tisk promenne cele_jmeno
cele_jmeno = jmeno + prijmeni
print (cele_jmeno)

# Vytvoreni a tisk promenne delka_jmena

print(len(cele_jmeno))

# Tisk ohranicene promenne cele_jmeno
delka = len(cele_jmeno)

print(delka * '=')
print(cele_jmeno)
print(delka * '=')