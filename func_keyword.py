def func(a, b=5, c=10):
    print('a is {0} and b is {1} and c is {2}'.format(a, b, c))


func(3, 7)
func(25, c=24)
func(c=50, a=100)
