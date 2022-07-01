"""
File: prime_checker.py
Name: Lina Chou
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

"""
概念:將輸入的值(被除數)除上2,依序除至輸入值的前一個值(1以及自己以外的除數)，例:輸入17,則從2.3.4...開始除至16，若餘數接不為0
	則判斷輸入值(被除數)為質數；反之。
流程:
1.請使用者輸入數字
2.若輸入值除2取餘數,若餘數為0,則印出「此數值不為質數」
3.若餘數不為0,則將除數+1,再次執行取餘數的動作
4.直到除數加至等同被除數,判斷過程中皆未有除數將其整除,則印出「此數值為質數」
5.輸入EXIT的值,方可印出「Have a good one!」並結束此程式


Concept:Let the inputting number divided by 2.3.4...in sequence.(except 1 & inputting number itself)
		If remainder is not 0 in the whole process,we can perceive it as a prime number.On the other hand, we won't
		see it as a prime number.
		
Process:
1.Let user input a number.
2.If it is divisible by 2,print "This is not a prime number."
3.If there is a remainder after dividing, do division again.
4.Do the division until the dividend is equal to the divisor, then print"This is a prime number."
5.If you wanna end this, input EXIT to print "Have a good one!" in the end.

"""

EXIT = -100


def main():
	print("Welcome to the prime checker!")
	number = int(input("n: "))
	num2 = 2  # 初始的除數
	while True:
		if number == EXIT:  # 輸入EXIT即可跳出迴圈
			break
		elif num2 == number:  # 當除數等於被除數時,判斷過程中沒有數可將輸入值整除,即為質數
			print(str(number)+" is a prime number.")
			number = int(input("n: "))
			num2 = 2  # 重設除數為2
		elif number % num2 == 0:  # 若可被整除,餘數為零,則不為質數
			print(str(number)+" is not a prime number.")
			number = int(input("n: "))
			num2 = 2  # 重設除數為2
		else:
			num2 += 1  # 若輸入值除上除數仍有餘數,則將除數+1,重複取餘數的動作
	print('Have a good one!')


if __name__ == "__main__":
	main()
