file = open("C:\\Users\\phakr\\Desktop\\python.txt", 'w')

#your code goes here
title = ""

for line in file:
    for word in line.split():
        title += word[0]
    print(title)
    title = ""


file.close()