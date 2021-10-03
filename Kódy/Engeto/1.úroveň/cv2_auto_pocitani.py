# Cenik
mercedes    = 150000
rolls_royce = '400000'
vybava = 50000

mercedes    = 150000
rolls_royce = '400000'
rolls = int(rolls_royce)
vybava = 50000

# 1. Cenu za dva Mercedesy,
# 2. cenu za Mercedes a Rolls-Royce,
# 3. cenu za dva Rolls-Royce s příplatkovou výbavou (každý z nich),
# 4. cenu za Mercedes s příplatkovou výbavou.
# 5. následně vytvoř proměnnou, která si od uživatele vyžádá libovolnou slevu na mercedes a do další proměnné ulož slevu na mercedes.

prvni = mercedes * 2
druhy = mercedes + rolls
treti = (rolls + vybava) * 2
ctvrty = mercedes + vybava
paty = int(input('Jakou chcete slevu za Meďoura? (v Eurech) '))

print('Dva mercedesy stojí', prvni)
print('Když si koupim Mercedes a Rolls Royce, tak mě to bude stát', druhy)
print('Dva Rolls-Royci v plný palbě stojí', treti)
print('Meďoura s výbavou koupím za', ctvrty)
print('Po slevě mě Mercedes bude stát', mercedes - paty)
