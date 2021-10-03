# Napiš program, který tiskne celá čísla od 1 do 100 (včetně).
# pro násobky 3 vytiskni Fizz (namísto čísla)
# pro násobky 5 vytiskni Buzz (namísto čísla)
# pro násobky 3 a 5 zároveň vytiskni FizzBuzz (namísto čísla)

for x in range(1,101):
    if x % 5 == 0 and x % 3 == 0:   # nebo x % 15 == 0
        print('Fizzbuzz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0:
        print('Fizz')
    else:
        print(x)
    
    
