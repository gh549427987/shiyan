import curses
from random import randrange, choice
from collections import defaultdict

actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
action_dict = dict(zip(letter_codes, actions * 2))
print(action_dict)

def main(stdscr):
    def init():
        '''init'''
        return 'Game'

    def not_game(state):
        responses = defaultdict(lambda: state)

        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]

    def game():
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
            if gamewin:
                return 'Win'
            if gamelose:
                return 'Lose'
        return 'Game'

    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
            }
    state = 'Init'

    while state != 'Exit':
        state = state_actions[state]()

def get_user_action(keyboard):
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]

class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = 2048
        self.score = 0
        self.highscore = 0
        self.reset()

def spawn(self):
    new_element = 4 if randrange(100) > 89 else 2
    (i,j) = choice([(i,j) for i in range(self.width) for j in range(self.height) if self.field[i][j] == 0])
    self.field[i][j] = new_element

def reset(self):
    if self.score > self.highscore:
        self.highscore = self.score
    self.score = 0

    self.field = [[0 for i in range(self.width)] for j in range(self.height)]
    self.spawn()

def move_row_left(row):
    def tighten(row):
        new_row = [i for i in row if i != 0]
        new_row += [0 for i in range(len(row) -len(new_row))]
        return new_row

    def merge(row):
        pair = False
        new_row = []
        for i in range(len(row)):
            if pair:
                new_row.append(2*row[i])
                self.score += 2*row[i]
                pair = False
            else:
                if i+1< len(row) and row[i] == row[i+1]:
                    pair = True
                    new_row.append(0)
                else:
                    new_row.append(row[i])
        assert len(new_row) == len(row)
        return new_row

    return tighten(merge(tighten(row)))
