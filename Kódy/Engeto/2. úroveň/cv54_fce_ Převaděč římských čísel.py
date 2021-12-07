def to_arab(arab: str):
    assert type(arab) == str, 'Potřebujeme string'
    result = 0
    numbers1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    numbers2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    while arab:
        if arab[:2] in numbers2:
            num = arab[:2]
            arab = arab[2:]
            number = numbers2
        else:
            num = arab[:1]
            arab = arab[1:]
            number = numbers1

        result += number[num]
    return result


def to_roman(num:int):
    assert type(num) == int, 'Potřebujeme číslo'
    result = ''
    numbers = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
     900: 'CM', 1000: 'M'}
    for arab in sorted(numbers, reverse=True):
        roman = numbers[arab]
        result += num // arab * roman
        num = num % arab
    return result
