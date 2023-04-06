import random

def rps_game () :
    # r>s, s>p, p>r
    user = input ("Enter 'r' for rock, 'p' for paper, 's' for scissors \n==> ")
    comp = random.choice (['r', 'p', 's'])

    if (user == comp) :
        return "It's a Tie"
    elif (play_game (user, comp) is True) :
        return f'You won, congrats(:'
    return f'You lost ):, try again...'


def play_game (player1, player2) :
    if (player1 == 'r' and player2 == 's') or (player1 == 's' and player2 == 'p') or (player1 == 'p' and player2 == 'r') :
        return True
    
    return False



print (rps_game ())




# Another Solution



def get_winner (p1, p2) :
    if (p1 == p2) :
        return "It's a tie!"
    
    elif (p1 == 'rock') :
        if (p2 == 'scissors') :
            return "First player wins!"
        else :
            return "Second player wins!"
        
    elif (p1 == 'scissors') :
        if (p2 == 'paper') :
            return "First player win!"
        else :
            return "Second player wins!"
        
    elif (p1 == 'paper') :
        if (p2 == 'rock') :
            return "First player wins!"
        else :
            return "Second player wins!"
        
    else :
        return "Invalid input!"
    


player1 = input ('First player: rock, paper or scissors: ')
player2 = input ('Second player: rock, paper or scissors: ')

print (get_winner (player1, player2))