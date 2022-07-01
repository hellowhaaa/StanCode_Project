"""
File: quadratic_solver.py
Name: Lina Chou
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
import math
"""
1. 請使用者輸入三個數字
2. 開根號的內容需為正，算式才能執行
3. 當開根號為正，個別計算x的值
4. 由 b*b-4*a*c 判斷，印出個別得到的x值 

1. Let user input three numbers.
2. b*b-4*a*c should be positive or the value can not be calculated.
3. Get the value of x respectively.
4. Print how many roots does the number have and the value of x.
"""


def main():
	print("stanCode Quadratic Solver!")
	a = float(input("Enter a: "))
	b = float(input("Enter b: "))
	c = float(input("Enter c: "))
	if b*b-4*a*c >= 0:
		y = math.sqrt(b*b-4*a*c)
		x1 = ((-1)*b+y)/(2*a)
		x2 = ((-1)*b-y)/(2*a)
	if b*b-4*a*c == 0:
		print("One root: "+str(x1))
	elif b*b-4*a*c > 0:
		print("Two roots: " + str(x1)+","+str(x2))
	elif b*b-4*a*c < 0:
		print("No real roots")


if __name__ == "__main__":
	main()
