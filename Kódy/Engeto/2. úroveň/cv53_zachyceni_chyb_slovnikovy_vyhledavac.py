def hledej_smudlo(key, value, dict):
    try:
        if dict[key] == value:
            return True
        else:
            return False
    except KeyError:
        print(f"Klíč '{key}' nenalezen")
        return False

muj_slovnik = {
    'jmeno':'Pepa',
    'prijmeni': 'Novak',
    'rok_narozeni': 1990,
    'mesto': 'Praha',
    'domaci_mazlicek': 'Chameleon'
}

hledej_smudlo('name', 'TondA', muj_slovnik)