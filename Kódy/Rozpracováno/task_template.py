# 1. Na začátku přivítá uživatele.
print()
print('*' * 12)
print('Ahoj, vítej!')
print('*' * 12)
print()
# 2. Vyžádá si od uživatele přihlašovací jméno a heslo.
jmeno = input('Nejdřív zadej uživatelské jméno: ')
heslo = input('Teď zadej i heslo:')

# 3. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.
    # Registrovaná uživatelská jména s hesly:
    # | USER |   PASSWORD  |
    # -----------------------
    # | bob  |     123     |
    # | ann  |    pass123  |
    # | mike | password123 |
    # | liz  |    pass123  |

uzivatel = {'bob':'123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

if uzivatel.get(jmeno) == heslo:
    print('Pojď dál!!!')
else:
    print('Padej vocuď!!!')
    quit()

print()
# 4. Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné
print('Teď si vyber jeden ze tří textů. To, že nevíš jaký, nevadí. Budeš si tipovat!')
print('*' * 77)
print('*' * 77)

'''
author = 
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]



vyber = int(input('Vyber si jeden ze tří textů. Napiš číslo od 1 do 3: '))
text = []

if vyber == 1:
    text = TEXTS[vyber - 1]
elif vyber == 2:
    text = TEXTS[vyber - 1]
elif vyber == 3:
    text = TEXTS[vyber - 1]
else:
    ('Vybral jsi neplatný text. Opakuj znovu.')

print('_' * 80)
print('_' * 80)
print(text)

# Pro vybraný text spočítá následující statistiky:
### počet slov,
### počet slov začínajících velkým písmenem,
### počet slov psaných velkými písmeny,
### počet slov psaných malými písmeny,
### počet čísel (ne cifer!).

print('*' * 80)
print('*' * 80)

rozdeleny_text = text.split()

ocisteny_text = []

while rozdeleny_text:
    text_bez_znaku = rozdeleny_text.pop()
    text_bez_znaku = text_bez_znaku.strip('.,?-!/')
    ocisteny_text.append(text_bez_znaku)

print(f"Počet slov je {len(ocisteny_text)}.")

list_pro_graf = ocisteny_text.copy

prvni_velke = []
jen_velke  = []
jen_male = []
cisla = []

while ocisteny_text:
    slovo = str(ocisteny_text.pop())
    if slovo.istitle()== True:
        prvni_velke.append(slovo)
    elif slovo.isupper() == True:
        jen_velke.append(slovo)
    elif slovo.islower() == True:
        jen_male.append(slovo)
    elif slovo.isdigit() == True:
        cisla.append(slovo)


print(f"Počet slov, které začínají na velké písmeno, je {len(prvni_velke)}.")
print(f"Slov, které mají jen velké písmena je {len(jen_velke)}.")
print(f"Celkový počet slov, které mají jen malá písmena, je {len(jen_male)}.")
print(f"Čísel je ve vybraném textu {len(cisla)}.")


# Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu




# součet všech čísel (ne cifer!) v textu
