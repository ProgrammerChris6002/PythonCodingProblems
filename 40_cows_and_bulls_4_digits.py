import random


def bulls_and_cows () :
    secret_number = str (random.randint (1000, 9999))
    print (secret_number)
    print ("Guess the number (Hint -> 4 Digits Number)")
    trials = 7

    while trials > 0 :
        guess_number = input ('Guess the number ==>: ')

        if (secret_number == guess_number) :
            print ('You guessed he number correctly!\nYOU WON.')
            break

        else :
            bulls, cows = 0, 0

            for i in range (len (secret_number)):
                if (secret_number[i] == guess_number[i]):
                    bulls += 1
                elif (guess_number[i] in secret_number):
                    cows += 1

        print (f"Bulls = {bulls}")
        print (f"Cows = {cows}")

        trials -= 1
    
    if (trials < 1) :
        return f'The number is {secret_number}.\nYou lost, better luck next time!!!'



print (bulls_and_cows ())




# Another Solution



secret_number = str (random.randint (1000, 9999))
print ("Guess the number. It contains 4 digits.")

remaining_try = 7

def get_bulls_cows (number, user_guess):
    bull_cows = [0,0] # cows, then bulls

    for i in range (len (number)):
        if (user_guess[i] == number):
            bull_cows[0] = 1
        elif (user_guess[i] in number):
            bull_cows[1] += 1

    return bull_cows


while remaining_try > 0:
    player_guess = input ("Enter your guess: ")

    if (player_guess == secret_number):
        print ("Yay, you guessed it!")
        print ("YOU WIN!")
        break
    else:
        bulls_cows = get_bulls_cows (secret_number, player_guess)

        print ("Bulls: ",bulls_cows[0])
        print ("Cows: ",bulls_cows[1])

        remaining_try -= 1

        if (remaining_try < 1):
            print ("You lost the game.")
            break