import random

def is_valid_play(play):
    return play in['rock', 'paper', 'scissors']

def random_play():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_game_result(human, computer):
    if human == computer:
        return 'tie'
    elif human == 'rock':
        if computer == 'paper':
            return 'computer'
        elif computer == 'scissors':
            return 'human'
    elif human == 'paper':
        if computer == 'rock':
            return 'human'
        elif computer == 'scissors':
            return 'computer'

    elif human == 'scissors':
        if computer == 'rock':
            return 'computer'
        elif computer == 'paper':
            return 'human'

# load je dependence ijnections (nevyhoda, ze jsem musela ve funkci neco zmenit
def main(load = input):
    human = None
    while not is_valid_play(human):
        human = load('rock, paper or scissors? ')

    computer = random_play()
    print(computer)
    result = determine_game_result(human,computer)
    print(result, 'is the winner')



#  co je pod tímto, nespouští v testu
if __name__ == '__main__':
    main()

