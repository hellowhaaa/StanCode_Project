"""
File: narcissistic_checker.py
Name: Arya Chou
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""
EXIT = -100


def main():
    print("Welcome to the narcissistic checker!")
    number = int(input("n: "))
    a = 10  # 除數 初始值為10
    times = 0  # 迴圈次數也就是次方
    while True:
        if number == EXIT:
            print("Have a good one!")
            break
        n = number // a  # 拿10,100,1000去除
        times += 1  # times 為次方 ,以153為例,求出次方為3
        a *= 10
        if n == 0:  # 直到前一個位數為0
            total = 0  # total為1**3等等
            number_new = number
            while a > 1:  # 若輸入153 a為1000
                a //= 10
                we = number_new // a  # 求出百位數為1 十位數為5 個位數為3
                rest = number_new % a  # 餘數
                number_new = rest  # 讓餘數等於number_new
                each = we ** times  # each 各個位數的次方
                total += each
            if total == number:
                print(str(number)+" is a narcissistic number")
            else:
                print(str(number)+" is not a narcissistic number")
            number = int(input("n: "))
            a = 10
            times = 0


"""
EXIT = -100

def main():
    print("Welcome to the narcissistic checker!")
    number = int(input("n: "))
    a = 10
    times = 0
    while True:
        if number == EXIT:
            print("Have a good one!")
            break
        n = number // a  # 拿10,100,1000去除
        times += 1  # times 為次方 ,以153為例,求出次方為3
        a *= 10
        if n == 0:  # 直到前一個位數為0
            total = 0  # total為1^
            while a > 1:  # 若輸入153 a為1000
                a //= 10
                we = number // a  # 求出百位數為1 十位數為5 個位數為3
                rest = number % a  # 餘數
                number = rest  # 讓餘數等於number
                each = we ** times
                total += each
            print(str(total))
            break
"""
if __name__ == '__main__':
    main()
