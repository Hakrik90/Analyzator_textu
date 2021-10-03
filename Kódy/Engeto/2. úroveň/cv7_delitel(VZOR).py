start = int(input('START: '))
stop = int(input('STOP: '))
divisor = int(input('DIVISOR: '))
result = []
if divisor:
    for num in range(start,stop+1):
        if num % divisor == 0:
            result.append(num)
    print('Numbers in range(' + str(start) +', ' + str(stop) + ') divisible by ' + str(divisor) + ':')
    print(result)
else:
    print('Cannot divide by zero')