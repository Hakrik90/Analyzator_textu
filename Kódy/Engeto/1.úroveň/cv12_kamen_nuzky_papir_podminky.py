# Naimportuj modul random
import random

# Vytvort list moznosti
moznosti = ['kámen', 'nůžky', 'papír']

# Vytvort promennou hrac
hrac = input("Napiš 'kámen', 'nůžky' nebo 'papír': ")

# Vytvort promennou pocitac
pocitac = random.choice(moznosti)

# Vytiskni volbu cloveka a pocitace
print('Hráč vybral:', hrac.capitalize())
print('Počítač vybral:', pocitac.capitalize())

# Vytvor podminku, zda hrac zvolil neplatnou volbu
if hrac != 'kámen' and hrac != 'nůžky' and hrac != 'papír':
    print("Neplatná volba! Napiš to správně")

# Pokud je volba v poradku, muzeme provest zbytek programu


# Podimky zahrnujici ruzne kombinace voleb hrace a pocitace a tisk vysledku
if hrac == pocitac:
    print('Nerozhodně!')
elif hrac == 'kámen' and pocitac == 'nůžky': #hráč kámen, počítač nůžky
    print('Ztupil jsi nůžky. Vyhrál jsi!')
elif hrac == 'kámen' and pocitac == 'papír': #hráč kámen, počítač papír
    print('Zabalil tě. Počítač vyhrál!')
elif hrac == 'nůžky' and pocitac == 'kámen': #hráč nůžky, počítač kámen
    print('Jsi tupej! Prohrál jsi!')
elif hrac == 'nůžky' and pocitac == 'papír': #hráč nůžky, počítač papír
    print('Přefikl jsi ho! Vyhrál jsi!')
elif hrac == 'papír' and pocitac == 'kámen': #hráč papír, počítač kámen
    print('Zabalil jsi to! Vyhrál jsi!')
elif hrac == 'papír' and pocitac == 'nůžky':
    print('Nechal jsi se přefiknout. You lose!')


