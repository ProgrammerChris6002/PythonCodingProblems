import random

def guess_game () :
    rand_num = random.randint (1, 10)
    score = 0
    guess = input ('Guess a number between 1 and 10==> ')

    if (guess == str (rand_num)) :
        rand_num = random.randint (1, 10)
        score += 10
        print ("Your score = " + score)
    elif (guess == 'q') :
        print ('Game Over.')
    else :
        print ('Try again...')

    while (guess != 'q') :
        guess = input ('Guess a number between 1 and 10, Enter \'q\' to exit==> ')
        if (guess == str (rand_num)) :
            rand_num = random.randint (1, 10)
            score += 10
            print (f"Your score = {score}")
        elif (guess == 'q') :
            print ('Game Over.')
        else :
            print ('Try again...')



guess_game ()




# Another Solution



print ('To stop anytime, enter: q')
score = 0

while True :
    num = random.randint (0,10)
    guess = input ("Guess a number betweeb 0 to 10: ")

    if (guess == 'q') :
        print ('Game Over.')
        break
    guess_num = int (guess)

    if guess_num is num :
        print ('CONGRATS, you guessed it correctly')
        score += 10
        print ('Your new score: ')
    else :
        print ('Your guess did not match')
        print ('The number was:', num)