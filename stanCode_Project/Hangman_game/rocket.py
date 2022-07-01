"""
File: rocket.py
Name: Lina Chou
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
"""
目的: 製造出一個火箭圖樣
流程: 可以更改SIZE 改變火箭大小

Purpose: Create the pattern of rocket.
Process: Change the rocket's size by inputting different number.

"""


# This constant determines rocket size.
SIZE = 3


def main():
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	for i in range(1, SIZE+1):
		for k in range(SIZE+1-i, 0, -1):
			print(" ", end="")
		for k in range(i):
			print("/", end="")
		for k in range(i):
			print('\\', end="")
		print("")


def belt():
	print("+", end="")
	for i in range(SIZE*2):
		print("=", end="")
	print("+")


def upper():
	for i in range(1, SIZE+1):
		print("|", end="")
		for k in range(0, SIZE-i):
			print(".", end="")
		for k in range(i):
			print("/", end="")
			print("\\", end="")
		for k in range(0, SIZE-i):
			print(".", end="")
		print("|")


def lower():
	for i in range(SIZE, 0, -1):
		print("|", end="")
		for k in range(SIZE-i):
			print(".", end="")
		for k in range(i):
			print("\\", end="")
			print("/", end="")
		for k in range(SIZE-i):
			print(".", end="")
		print("|")





"""


def main():
	st = 'stanCode'
	first = st[0]
	last = st[7]
	last2 = st[len(st)-1]

	print(str(first)+str(last)+str(last2))
	length = len(st)

	print(str(length))






	s = 'sXanXode'
	print(str(s))
	ans = ""
	for i in range(len(s)):
		ch = s[i]
		if ch == 'X':
			ans += 'C'
		else:
			ans += ch
	print(str(ans))

"""



"""
def main():
	for j in range(5):
		print(str(j), end="") # 01234
	print("")
	for i in range(1, 4):
		print(str(i), end="")
	print("")
	for k in range(1, 12, 2):
		print(str(k), end="")
	print("")

	for a in range(3):
		for b in range(4):
			print("#", end="")
		print("")

	for c in range(3):
		for d in range(c+1):
			print("#", end="")
		print("")

	for e in range(4):
		for f in range(4):
			if (e+f) % 2 == 0:
				print("#", end="")
			else:
				print(' ', end="")
		print("")
		
"""

"""
def main():
	a = 0
	a = plus_one(8)
	print(str(a))


def plus_one(a):
	a += 1
	return a


"""
"""
def main():
	a = 0
	plus_one()
	
	
def plus_one(a):
	a += 1
	print(str(a))

"""



###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()