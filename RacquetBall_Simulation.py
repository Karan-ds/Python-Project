# Computer Simulation Program - A robust framework technique to solve real world problems through simulating  random
# Scenarios.

# Top-Down design Base Algorithm Structure
# Program simulates Win Probability for RacquetBall based on WinServe probability

from random import random


def main():  # Main function for simulating the problem
    intro()
    prob_A, prob_B, no_of_game = getinputs()
    A, B = sim_game(prob_A, prob_B, no_of_game)
    report_card(A, B)


def intro():
    print('This Program simulates RACQUETBALL.')
    print('Simulation is done on basis of probability of winning serves.')
    print('For Simplicity of results, Player-A will always serve first.')


def getinputs():
    prob_A = float(input('Enter Probability for A: '))
    prob_B = float(input('Enter Probability for B: '))
    n = int(input('Enter total number of games for simulation: '))
    return prob_A, prob_B, n


def sim_game(x, y, z):
    win_A = 0
    win_B = 0
    for i in range(z):
        a, b = sim_i_game(x, y)
        if a > b:
            win_A += 1

        elif b > a:
            win_B += 1

    return win_A, win_B


def sim_i_game(a, b):
    score_A = 0
    score_B = 0
    serving = 'A'
    while not game_over(score_A, score_B):
        if serving == 'A':
            if random() < a:
                score_A += 1
            else:
                serving = 'B'
        elif serving == 'B':
            if random() < b:
                score_B += 1
            else:
                serving = 'A'

    return score_A, score_B


def game_over(a, b):
    return (a == 15) or (b == 15)


def report_card(a, b):
    f = a + b
    print('Number of games simulated: ', f)
    print('Player - A won:{} ({}%) '.format(a, (a / f) * 100))
    print('Player - B won:{} ({}%) '.format(b, (b / f) * 100))


if __name__ == '__main__':
    main()

# Sample Prog -
# Prob - A = 0.65
# Prob - B = 0.6
# No of games Simulated - 5000
