# Ukladani jmena
jmeno = input("Jak se jmenuješ(křestní)? ")

# Tisk jmena
print(jmeno)

# Ukladani prijmeni
prijmeni = input("Jaké je tvé příjmení? ")

# Tisk prijmeni
print(prijmeni)

# Vytvoreni a tisk promenne cele_jmeno
cele_jmeno = jmeno + ' ' + prijmeni

# Vytvoreni a tisk promenne delka_jmena
delka_jmena = len(cele_jmeno)
print("Délka jména:",delka_jmena)

# Tisk ohranicene promenne cele_jmeno
print('=' * delka_jmena)
print(cele_jmeno)
print('=' * delka_jmena)

