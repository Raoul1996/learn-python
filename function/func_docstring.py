def print_max(x, y):
    '''Print the maximum number.
    :param x: {Integer}
    :param y: {Integer}
    :return: {Integer}
    '''
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


print_max(3, 5)
print(print_max.__doc__)
