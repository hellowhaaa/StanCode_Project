"""
File: hangman.py
Name: Lina Chou
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""
import random
# This constant controls the number of guess the player has.
"""
流程:
1. 告知使用者要猜的字樣以及猜測次數
2. 進入迴圈請使用者猜測字母,若使用者輸入錯誤,則請使用者重新輸入
3. 使用right_or_not function 個別做出猜測對與錯的回應
4. 若猜錯次數大於上限值,則break, 並印出You are completely hung : ( 
5. 若猜中單字,則break, 並印出You win!!
6. 告知使用者 猜測的單字為何

Process:
1. Inform user what word is he/she going to guess and guessing limit.
2. Use while loop to let user guess. If user inputs the wrong guess, ask he/she inputs again.
3. Use function right_or_not to see if user guess right.
4. If the times that user guess wrong is over the upper limit then print 'You are completely hung : ('.
5. If user guesses the word, then print 'You win!!'
6. Inform user what word did she/he guessed.
"""


N_TURNS = 7


def main():
    s = random_word()
    print('The word looks like: ' + dash(s))
    new_line = dash(s)
    n_turn = N_TURNS
    while True:
        if n_turn > 0:
            print("You have " + str(n_turn) + 'guesses left')
            guess = input('Your guess: ')
            big_guess = guess.upper()
            new_line = in_or_not(big_guess, s, new_line)
            print('The word looks like: ' + new_line)
            if s.find(big_guess) == -1:
                n_turn -= 1
            if new_line == s:
                print('you win')
                break
        else:
            print('You are compltetely hung')
            break



def dash(word):
    line = ""
    for i in range(len(word)):
        line += '-'
    return line


def in_or_not(big_guess, s, new_dash):
    if s.find(big_guess) != -1:
        print('You are correct!')
        new = ""
        for i in range(len(s)):
            ch = s[i]
            if big_guess == ch:
                new += big_guess
            else:
                new += new_dash[i]
        return new
    else:
        print('There is no ' + big_guess + 'in the word.')
        return new_dash




def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


if __name__ == '__main__':
    main()
