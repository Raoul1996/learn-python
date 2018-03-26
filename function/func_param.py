def print_max(a, b):
    if a > b:
        print('{} is maximum'.format(a))
    elif a == b:
        print('{0} is equal to {1}'.format(a, b))
    else:
        print(b, 'is maximum')


print_max(3, 3)
