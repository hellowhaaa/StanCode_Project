"""
File: hailstone.py
Name: Lina Chou
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

"""
概念:判斷輸入的值為奇數偶數,若為奇數則值*3+1,若為偶數則/2,再利用while迴圈持續判斷奇偶、計算數值、紀錄迴圈次數,直到計算值為1
Concept: Identify if inputting number is odd number or even number. If it is odd number, then multiply 3 and plus 1.
If it is even number, then divide 2. Use while loop to identify the number is odd or even,calculate number, 
count the times of while loop until the last value is 1.

流程:
1.請使用者輸入一數字
2.判斷奇數偶數,若為奇數則該數值乘三加一,若為偶數則除二
3.分別印出計算過後的值
4.再次判斷奇數偶數並重複第2.3步驟直到最後數直為1
5.使用a+=1紀錄迴圈次數,並印出「達到1的步驟次數」

Process:
1. Let user input a number.
2. Identify if inputting number is odd or even.
3. Print each value after calculating.
4. Repeat step2 & step3 until the last value is 1.
5. Use a+=1 to count the times and print "How many steps to reach 1." 

"""


def main():
    print("This program computes Hailstone sequences.")
    print("")
    number = int(input("Enter a number: "))
    dev = number % 2  # 除2取餘數判斷奇數或偶數
    a = 0  # 紀錄次數的初始值為零
    while number > 1:  # 因最後欲得出值為1,則number必大於1,否則會跑進迴圈做運算
        a += 1  # 每跑一次while loop,就加一次,方可知道達到數值1, 要做幾次迴圈
        if dev == 0:  # 若餘數為0,則為偶數
            get_even = number // 2
            print(str(number)+" is even,so I take half:  "+str(get_even))
            dev = get_even % 2  # 除2取餘數判斷奇數或偶數
            number = get_even  # 將計算後的值重新assign給number
        else:  # 若餘數不等於0,則為奇數
            get_odd = number * 3 + 1
            print(str(number)+" is odd, so I make 3n+1:  " + str(get_odd))
            dev = get_odd % 2  # 除2取餘數判斷奇數或偶數
            number = get_odd  # 將計算後的值重新assign給number
        if number == 1:  # 若輸入值為1,則跳脫迴圈
            break
    print("It took "+str(a)+" steps to reach 1.")  # 印出次數


if __name__ == "__main__":
    main()
