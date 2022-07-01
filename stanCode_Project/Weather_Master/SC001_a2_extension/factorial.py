"""
File: factioral.py
Name: Arya Chou
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""
"""
概念:若輸入一數值不等於EXIT,則進入迴圈,指派value為兩數相乘, 得出的新數值則和下一個新輸入的數值相乘直到使用者輸入EXIT的數值
Concept: If inputting number doesn't equal to EXIT, then run while loop. Lut odd and new number multiply each other
to get answer until user inputs EXIT to end it.


流程:
1. 請使用者輸入一數字
2. 若為EXIT 數值則印出------ See ya! ------- 反之則印出輸入數值並進入迴圈
3. 請使用者再次輸入新數字,輸入的新數值和舊數值相乘並印出其答案
4. 指派答案為舊數值, 再次請使用者輸入新數值,並使其相乘,印出答案
5. 當使用者輸入EXIT數值跳脫迴圈,印出------ See ya! -------,結束程式
Process:
1. Let user input a number.
2. If inputting number equals EXIT, print------ See ya! ------- ,or prints what user input than run while loop.
3. Let user input a number again,print the value after multiplying old and new number.
4. Assign the answer as old number and let user input new number again.
5. While user inputs EXIT ,prints------ See ya! ------- , and end this.
"""


EXIT = -100


def main():
	print("Welcome to stanCode factorial master!")
	num = int(input("Give me a number, and I will list the answer of factorial: "))
	if num == EXIT:
		print("------ See ya! -------")
	else:  # 若輸入值不為EXIT
		print("Answer: " + str(num))
		while num != EXIT:  # 當輸入值不為EXIT,則執行While 迴圈
			num2 = int(input("Give me a number, and I will list the answer of factorial: "))
			if num2 == EXIT:  # 當輸入值為EXIT,則break 跳脫迴圈
				print("------ See ya! -------")
				break
			value = num * num2  # 使舊的數值(num) 乘新的數值(num2)
			print("Answer: " + str(value))
			num = value  # 指派舊數值num為相乘後的結果


"""

平均值練習~~~~
def main():
	num1 = int(input("Input a number:"))
	num2 = int(input("Input a number:"))
	ave = average(num1, num2)
	print("平均值為"+str(ave))


def average(a,b):
	ans = (a+b)/2
	return ans

"""

if __name__ == '__main__':
	main()