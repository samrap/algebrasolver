import os
import random

"""Sam Rapaport's Tic-Tac-Toe

A poorly hacked Tic-Tac-Toe game with a terrible function for
checking if there is three in a row.
"""
board = []

def set_board():
    board = [
        ' ', ' ', ' ',
        ' ', ' ', ' ',
        ' ', ' ', ' '
    ]
    return board

def clear(numlines=120):
    """Clear the screen of all output.
    numlines is an optional fallback parameter.
    Credit to Jon Cage on SO for answering someone's
    question about this.
    """

    # Unix, OSX, Linux
    if os.name == 'posix':
        os.system('clear')

    # DOS/Windows
    elif os.name in ('nt', 'dos', 'ce'):
        os.system('CLS')

    # Fallback
    else:
        print '\n' * numlines

def print_board():
    print '\n'
    print '    1   2   3'
    print ''
    print 'A  ', board[0], '|', board[1], '|', board[2]
    print '   -----------'
    print 'B  ', board[3], '|', board[4], '|', board[5]
    print '   -----------'
    print 'C  ', board[6], '|', board[7], '|', board[8]
    print '\n'

def is_taken(index):
    if board[index] != 'X' and board[index] != 'O':
        return False
    return True

def cat():
    if all(x != ' ' for x in board):
        return True
    return False

def in_row(obj, num=3):
    """Find if there are num amount three of obj (x, y)in a row.

    Each item in the rangelist list is a possible 3-in-a-row win and the index
    in each set is checked on each iteration through the for loop.
    """

    rangelist = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    if num == 3:
        for numset in rangelist:
            if (board[numset[0]] == obj and board[numset[1]] == obj and
                board[numset[2]] == obj):
                return True

    if num == 2:
        # I apologize for this mess
        for numset in rangelist:
            if board[numset[0]] == obj and board[numset[1]] == obj:
                return (0, 1, numset[2])
            if board[numset[1]] == obj and board[numset[2]] == obj:
                return (1, 2, numset[0])
            if board[numset[0]] == obj and board[numset[2]] == obj:
                return (0, 2, numset[1])
        else:
            # Hard to explain why I can't just return False, but to make things
            # easy it has to be this way
            return None

    return False

def filter_input(usrin, holder):
    points = {
        'A1': 0, 'A2': 1, 'A3': 2,
        'B1': 3, 'B2': 4, 'B3': 5,
        'C1': 6, 'C2': 7, 'C3': 8
    }

    for p in points.keys():
        if usrin == p:
            if is_taken(points[usrin]):
                return False
            else:
                board[points[usrin]] = holder
                return True
    else:
        print "You entered the wrong points. Lose a turn!"

def AI_random():
    random.seed()
    point = random.randint(0, 8)
    if is_taken(point):
        AI_random()
    else:
        board[point] = 'O'

def AI_logic(player='X'):
    two = in_row(player, 2)
    if two != None:
        point = two[2]
        if is_taken(point) is True:
            if player == 'X':
                AI_logic('O')
            else:
                AI_random()
        else:
            board[point] = 'O'
    else:
        if player == 'X':
            AI_logic('O')
        else:
            AI_random()

def main_loop():
    while True:
        print_board()
        usrin = raw_input("Enter the point: ").replace(' ','')
        clear()

        if filter_input(usrin, 'X') is False:
            print "That point is already taken! Try again:"
            continue

        if in_row('X') is True:
            print "You win!"
            break
        if cat() is True: break
        AI_logic()
        if in_row('O') is True:
            print "You lose!"
            break
        if cat() is True: break
    else:
        print "Cats game!"


def play():
    global board;
    board = set_board()

    clear()
    main_loop()
    print "Game over! Final board:"
    print_board()

if __name__ == '__main__':
    play()
