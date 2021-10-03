#Začni tím, že si vytvoříš hlavní slovník do kterého budeš vkládat ostatní slovníky:
databaze = {'id123': {},'id124': {},'id125': {}}

#Pak deklaruj ostatní slovníky
slovnik1 = {'jmeno': 'Thomas', 'vek': 45, 'zeme': 'Czechia', 'mesto': 'Brno'}
slovnik2 = {'jmeno': 'Daniel', 'vek': 34, 'zeme': 'Czechia', 'mesto': 'Prague'}
slovnik3 = {'jmeno': 'Eva', 'vek': 43, 'zeme': 'Czechia', 'mesto': 'Olomouc'}

#Nakonec použij speciální metodu slovníku, kterou vložiš 3 výše uvedené slovníky jeden za druhým do hlavního
databaze['id123'] = slovnik1
databaze['id124'] = slovnik2
databaze['id125'] = slovnik3

print(databaze)



#Vzorové řešení

databaze = {'id123': {},'id124': {},'id125': {}}

slovnik1 = {'jmeno': 'Thomas', 'vek': 45, 'zeme': 'Czechia', 'mesto': 'Brno'}
slovnik2 = {'jmeno': 'Daniel', 'vek': 34, 'zeme': 'Czechia', 'mesto': 'Prague'}
slovnik3 = {'jmeno': 'Eva', 'vek': 43, 'zeme': 'Czechia', 'mesto': 'Olomouc'}

databaze.update(id123 = slovnik1)
databaze.update(id124 = slovnik2)
databaze.update(id125 = slovnik3)

print(databaze)



