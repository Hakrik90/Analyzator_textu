# Vytvoříme nový prázdný slovník a vložíme do něj kontakty
muj_slovnik = {}
kontakty = {"mobil": "+420582582582", "email": "matous@matous.cz"}
muj_slovnik["kontakt"] = kontakty

# Zobrazím všechny kontakty
print(muj_slovnik["kontakt"])

# Zobrazím mobil
print(muj_slovnik["kontakt"]["mobil"])

# Zobrazím email
print(muj_slovnik["kontakt"]["email"])