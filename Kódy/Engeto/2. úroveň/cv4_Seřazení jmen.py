# Vytvořme program, který nám seřadí abecedně jakýkoli list. Nemůžeme použít funkce jako je sort() nebo sorted(). Toto cvičení slouží jako procvičení práce s for + break + else.

# Vytvoř list, do kterého vložíš jeden prvek z list names. Zároveň ho z listu names odstraň. Tento krok se ti bude hodit, když budeš chtít přidávat a seřazovat další jméno z listu names do listu sorted_names

names = ['Michal', 'Pepa', 'Honza',
        'Pavel', 'Lukas', 'Matej',
        'Iva', 'Klara', 'Jana',
        'Honza', 'Vasek','Milan', 'Michal']

sorted_names = [names.pop(0)]

# vnější for loop, kterým budeš procházet seznam names (měl by mít už o jeden prvek méně)
for name in names:
    #vnitřní for loop, kterým budeš procházet seznam sorted_names a pomocí podmínkového výrazu, break a else vlož jméno z names buď na pozici, nebo za pozici
    for i,preparation in enumerate(sorted_names):
        if name < preparation:
            sorted_names.insert(i,name)
            break
    else:
        sorted_names.append(name)

print(sorted_names)



