sjednoceni = set('čaukymňauky').union(set('zdarec'), set('ahoj'))
print(sjednoceni)

prunik = set('čaukymňauky').intersection(set('zdarec'), set('ahoj'))
print(prunik)

rozdil = set('čaukymňauky').difference(set('zdarec'), set('ahoj'))
print(rozdil)

symetricky_rozdil = set('čaukymňauky').symmetric_difference(set('zdarec')) #Tento set bude obsahovat prvky, které sety nemají společné.
print(symetricky_rozdil)

podmnozina = set('čaukymňauky').issubset(set('zdarec')) #kontroluje, zda se všechny prvky jednoho setu nachází v setu druhém.
print(podmnozina)

disjunktivni_mnozina = set('čus').isdisjoint(set('zdarec')) #zkontroluje, zda dva nebo více setů nemají společný žádný prvek.
print(disjunktivni_mnozina)