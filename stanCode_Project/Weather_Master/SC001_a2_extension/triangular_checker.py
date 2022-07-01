"""
File: triangular_checker.py
Name: Arya Chou
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

"""
流程:
1. 請使用者輸入一數值,若此數值為EXIT number 則印出"Have a good one."
2. 使輸入值*2 判斷是否等於某數乘以某數加一(n*(n+1))
3. 若為n*(n+1)則印出「為三角形數」。反之則利用迴圈將n加一,若n等於輸入值,表示此為非三角形數,並印出「非三角形數」

Process:
1. Let user input a number, if it is EXIT number then print "Have a good one!" and end this program.
2. Multiply inputting number 2 to judge if it equals to a number multiply itself plus one. (n*(n+1))
3. If it equals to n*(n+1), print " is a triangular number.". On the other hands,utilize while loop plus 1 to n,
If n equals to inputting number, means it is not triangular number and print it out.  

"""
EXIT = -100


def main():

    print("Welcome to the triangular number checker!")
    number = int(input("n: "))
    n = 1  # 設某數初始值為1
    if number == EXIT:
        print("Have a good one.")
    while n <= number & number != EXIT:
        number1 = number * 2  # Assign number1 為輸入值乘2
        if number1 == n * (n + 1):  # 若number1等於n*(n+1),印出此為三角形數,並請使用者再次輸入一值
            print(str(number) + " is a triangular number.")
            number = int(input("n: "))
            n = 1  # 重設某數的初始值
        elif n == number:
            print(str(number) + " is not a triangular number.")
            number = int(input("n: "))
            n = 1  # 重設某數的初始值
        else:
            n += 1  # 若不為三角形數,則n加1,直到等於number
    print("Have a good one!")


### DO NOT EDIT THE CODE BELOW THIS LINE ###

if __name__ == '__main__':
    main()
