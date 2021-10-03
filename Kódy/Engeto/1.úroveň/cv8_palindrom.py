
slovo = input('Napiš nějaký slovo! ')

if slovo.casefold() == slovo.casefold()[::-1]:
    print(slovo, 'je palindrom!')
else:
    print(slovo, 'není palindrom!')