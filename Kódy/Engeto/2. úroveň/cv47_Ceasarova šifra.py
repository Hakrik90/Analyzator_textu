#Ceasarova šifra v praxi:

#S posunem o 3 DOLEVA (-3) by písmeno D bylo nahrazeno písmenem A, E by bylo nahrazeno B, atd.
#S posunem o 3 DOPRAVA (3) by písmeno D bylo nahrazeno písmenem G, E by bylo nahrazeno H, atd.



# Definice fce caesar
def caesar(message, step):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    code = []


    for l in message:
        if l.lower() in alphabet:
            i = alphabet.index(l.lower())
            if i+step < len(alphabet) and i+step >= 0:
                code.append(alphabet[i+step])
            else:
                code.append(alphabet[(i + step) % len(alphabet)])
        elif l != l.isalpha():
            code.append(l)

    code[-2] = code[-2].upper()
    return "".join(code)

# Zprava
message = 'abc def ghi jkl mno pqr stu vwx Yz'

print(caesar(message,3))