def sum_list(items: list):
    total = 0.0
    for i in items:
        try:
            total += float(i)
        except:
            continue
    return total

test = [1, 'asda', {'zvire':'kocka'}, '3.0', 2.0, [], '\n', '4']

print(sum_list(test))
