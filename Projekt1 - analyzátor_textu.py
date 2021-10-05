print()
users = {"bob":"123", "ann":"pass123","mike":"password123","liz":"pass123"}
separator = '-' * 50
name = input('Enter your username: ')
password = input('Enter your password: ')

print(separator)
if users.get(name) == password:
    print('Welcome to the app,', name)
else:
    print('Wrong name or password')
    quit()

print('We have 3 texts to be analyzed')
print(separator)

'''
author = 
'''
TEXTS = ['''Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, which traverse the valley. ''',

'''At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present.''']

cislo_text = input('Write a number from 1 to 3 to select the text: ')

if cislo_text.isdigit() == False: 
    print('You have to insert the number')
    quit()
elif int(cislo_text) > 0 and int(cislo_text) <= 3:
    text = TEXTS[int(cislo_text) - 1]
else: 
    print('Inserted number is out of range')
    quit()

print(separator)
print(text)
print(separator)


words = text.split()

clean_words = []
title = []
upper = []
lower_case = []
numbers = []

for word in words:
    word = word.strip('-,. ')
    clean_words.append(word)
    if word.isdigit():
        numbers.append(word)
    elif word.istitle():
        title.append(word)
    elif word.isupper():
        upper.append(word)
    elif word.islower():
        lower_case.append(word)
    

# pocet slov
print(f"There are {len(clean_words)} words in the selected text.")
# prvni velke
print(f"There are {len(title)} titlecase words.")
#jen velke
print(f"There are {len(upper)} uppercase words.")
#jen male
print(f"There are {len(lower_case)} lowercase words.")
#cisla
print(f"There are {len(numbers)} numeric strings.")
#suma
print(f"The sum of all numbers is {sum(int(x) for x in numbers)}.")

print(separator, separator, sep='\n')


occurencies = {}

for word in clean_words:
    if len(word) not in occurencies:
        occurencies[len(word)] = 1
    else:
        occurencies[len(word)] += 1

dict_items = occurencies.items()
sorted_items = sorted(dict_items)


print("LEN",'\t',"|","OCCURENCES".center(15),'\t',"|", "NR.")
print(separator)
for nr,count in sorted_items:
    print(str(nr).center(4),'\t', '|', ('*' * count).center(16),'\t' "|", count)
