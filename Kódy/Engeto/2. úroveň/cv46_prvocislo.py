#Funkce, která vygeneruje list prvočísel do specifikovaného čísla - list_primes.
#Funkce, která vyhodnotí, zda je dané číslo prvočíslem - is_prime.

# Definice fce list_primes
def list_primes(number):
    p = 2
    all = list(range(p,number+1))
    primes = set()

    while all:
        i = all.pop(0)
        primes.add(i)

        for num in all:
            if num % i == 0:
                all.remove(num)
    return primes

def is_prime(num):
    return num in list_primes(num+1)







