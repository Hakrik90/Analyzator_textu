import random

words = ['daddy', 'napkin', 'mountain', 'lumberjack', 'symphony', 'chicken', 'destiny', 'pride']

def sibenice(slova):
    slovo = random.choice(slova)
    status = ['_'] * len(slovo)
    pokusy = int(len(slovo) * 1.6)
    print('Přemýšlím nad slovem. Jaké je to slovo?')
    while True:
        pismeno = ziskej_pismeno(status, pokusy)
        zmena_pismena(pismeno, slovo, status)
        pokusy -= 1

        if '_' not in status:
            print('Gratuluju! Vše jsi uhádl!')
            break
        if not pokusy:
            print('Blbý! Došli ti pokusy!')
            break

def ziskej_pismeno(status, pokusy):
    print(''.join(status))
    pismeno = input('Hádej písmeno | Máš ještě tolik pokusů: ' + str(pokusy) + '\n')
    return pismeno

def zmena_pismena(pismeno, slovo, status):

    pocet_nahrazenych_pismen = 0

    for i,character in  enumerate(slovo):
        if character == pismeno:
            status[i] = character
            pocet_nahrazenych_pismen += 1

    if pocet_nahrazenych_pismen:
        print('Počet uhodnotých písmen:' + str(pocet_nahrazenych_pismen))

    else:
        print('Špatně! Písmeno', pismeno, 'není ve v hádaném slově.')


sibenice(words)

