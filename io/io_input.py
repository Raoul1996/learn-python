import re


def remove(text):
    return re.sub('\W', '', text)


def reverse(text):
    return remove(text)[::-1]


def is_palindrome(text):
    return remove(text) == reverse(text)


something = input("Enter text: ")

if is_palindrome(something):
    print('Yes ,it\'s a palindrome')
else:
    print('No it\'s not a palindrome')
