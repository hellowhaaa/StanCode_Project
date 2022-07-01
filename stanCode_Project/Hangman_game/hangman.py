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
    dash = first(s)  # 一條線
    print("The word looks like: " + dash)
    number = N_TURNS
    print("You have " + str(number) + " guesses left.")
    while True:
        guess = input("Your guess: ")
        identify(guess)  # 判斷使用者是否輸入正確
        new_guess = guess.upper()
        dash = right_or_not(new_guess, s, dash)  # 判斷猜測的對與錯
        number = loss_one_life(new_guess, s, number, dash)
        if number == 0:
            print("You are completely hung : ( ")
            break
        elif dash == s:
            print("You win!!")
            break
        else:
            print("The word looks like " + dash)
    print("The word was: "+s)


def first(s):  # 尚未猜測前的單字字樣都會是橫線
    an = ""
    for k in range(len(s)):
        an += '-'
    return an


def identify(guess):  # guess 有沒有輸入錯誤
    while not guess.isalpha() or len(guess) > 1:
        print("illegal format.")
        guess = input("Your guess: ")
    return guess


def right_or_not(new_guess, s, dash):  # 判斷猜測的對與錯
    if new_guess in s:
        pre_ans = dash
        ans = ""
        j = s.find(new_guess)
        for i in range(len(s)):
            ch = s[i]
            if ch == s[j]:
                ans += s[i]
            else:
                ans += pre_ans[i]
        dash = ans
        print("You are correct!")
        return dash
    else:
        for r in range(len(s)):
            print("There is no " + new_guess + "'s in the word.")
            return dash


def loss_one_life(new_guess, s, number, dash):
    if s.find(new_guess) != -1:
        if not dash == s:
            print("You have " + str(number) + " guesses left.")
    else:
        number -= 1
        if number > 0:
            print("You have " + str(number) + " guesses left.")
    return number


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
