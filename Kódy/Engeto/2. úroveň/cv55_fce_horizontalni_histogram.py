def horizont_hist(numbers:list):
    for n in numbers:
        n = int(n)
        print(f"|{'*' * n}")


horizont_hist([4,5,7,10,6,0,2])