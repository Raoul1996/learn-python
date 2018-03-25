number = 23
guess = int(input('Enter a integer : '))
if guess == number:
    print('Congratulations, you guessed it')
    print('(but you do not win any prizes!)')
elif guess < number:
    print('No, it\'s a little higher than that')
else:
    print('No, it\'s a little lower than that')
print('Done')

