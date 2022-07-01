"""
File: number_checker.py
Name: Lina Chou
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

"""
流程:
1. 讓使用者輸入一數值,若數值為EXIT,則印出"Have a good one!"結束程式
2. 當除數小於輸入值時,用While迴圈,持續取餘數為零的值(也就是因數)做加總
3. 依加總後的值,印出完全數,盈數還是虧數
4. 用while迴圈,讓使用者再次輸入一數值,直到輸入值為EXIT


Process:
1. Let user input a number, if it is EXIT number then print "Have a good one!" and end this program.
2. When divisor less than inputting number, use while loop. Find the all factors of the number and add them up.
3. Depend on each sum, print perfect number, abundant number or deficient number.
4. Use while loop to let user input number again until it is EXIT number.
"""


EXIT = -100


def main():
    print("Welcome to the number checker!")
    number = int(input("n:"))
    while True:
        if number == EXIT:  # 當輸入值為EXIT,則break 跳脫迴圈
            print("Have a good one!")
            break
        total = 0  # 設因數的加總為total,而初始值為0
        divider = 1  # 設除數為divider,而初始值為1
        while divider < number:  # 當除數小於使用者輸入的數時,執行以下迴圈去加總所有因數
            get = number % divider  # 取餘數
            if get == 0:  # 若get == 0 則判斷此除數為輸入值的因數
                total += divider
            divider += 1
        if total == number:
            print(str(number) + " is a perfect number.")
        elif total > number:
            print(str(number) + " is an abundant number.")
        else:
            print(str(number) + " is a deficient number.")
        number = int(input("n:"))


if __name__ == '__main__':
    main()
