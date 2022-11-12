import random
x = random.randrange(1,100)
guessRight = 0

while guessRight < 5:
    guess = int(input("Guess: "))
    guessRight += 1
    if guess < x:
        print('Your guess is too low')
    if guess > x:
        print('Your guess is too high')
    if guess == x:
        break
if guess == x:
    print('You guessed the number!')
else:
    print('You did not guess the number, The number was ' + str(x))
