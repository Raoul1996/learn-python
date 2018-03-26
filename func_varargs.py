def total(a=5, *numbers, **phoneBook):
    print('a', a)
    for single_item in numbers:
        print('single_item', single_item)
    for first_part, second_part in phoneBook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, 4, Jack=1123, Jone=2231, Ingel=1560))
