board = [
    ['X', ' ', ' '],
    [' ', 'X', ' '],
    [' ', ' ', 'X']
]

p = {
    'X': 1,
    'O': 0
}

TURN = 1
x,o = 'X', 'O'

def display():
    for row in board:
        print(row)

