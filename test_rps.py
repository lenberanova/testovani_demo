import rps
import pytest

def test_rock_is_valid_play():
    assert rps.is_valid_play('rock') is True

def test_paper_is_valid_play():
    assert rps.is_valid_play('paper') is True

def test_scissors_is_valid_play():
    assert rps.is_valid_play('scissors') is True

def test_abcd_is_valid_play():
    assert rps.is_valid_play('abcd') is False

def test_1234_is_valid_play():
    assert rps.is_valid_play('1234') is False

# tento test je na jeden tah, musel by se opakovat, musi tam byt vice opakovani pres konstantu
def test_random_play_is_always_valid():
    for i in range(1000):
        assert rps.is_valid_play(rps.random_play())

# hraje vsechny moznosti
def test_random_play_is_fair():
    plays = {
        'rock':0,
        'paper':0,
        'scissors':0
    }
    for i in range(10000):
        play = rps.random_play()
        plays[play] += 1
    for value in plays.values():
            assert value > 2000

def test_rock_rock_is_tie():
    assert rps.determine_game_result('rock', 'rock') == 'tie'

#parametricky dekorator, prožene tam všechny hodnoty
@pytest.mark.parametrize('play', ['rock', 'paper', 'scissors'])
def test_same_is_tie(play):
    assert rps.determine_game_result(play, play) == 'tie'

combination = [('scissors','paper'),
                            ('rock','scissors'),
                            ('paper','rock')]

@pytest.mark.parametrize('human, computer',
                         combination)
def test_human_wins(human, computer):
    assert rps.determine_game_result(human, computer) == 'human'

@pytest.mark.parametrize('computer, human',
                         combination)
def test_computer_wins(computer, human):
    assert rps.determine_game_result(human, computer) == 'computer'

