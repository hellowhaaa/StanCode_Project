"""
File: weather_master.py
Name: Arya Chou
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
"""
概念:若使用者輸入一非EXIT的值,則印出當中的最大值,最小值,平均氣溫以及低於16度的天數;若一開始便輸入EXIT的值,則不進入迴圈做計算。
Concept:According to what numbers user inputs, if they are not equal to EXIT,print maximum number, minimum number, 
average number,the days that temperature is lower than 16 degrees. On the other hands, it won't enter while loop 
to calculate.

流程:
1. 印出 「stanCode "Weather Master 4.0" !」,並請使用者輸入一數字
2. 若使用者輸入等於EXIT的數值,則不進入迴圈,印出No temperatures were entered
3. 若使用者輸入非EXIT的數值,則進入迴圈記錄當中的最大值,最小值,平均氣溫以及低於16度的天數
4. 分別印出最大值,最小值,平均氣溫以及低於16度的天數
Procedure:
1. Print "stanCode "Weather Master 4.0" !" anf let user input a number.
2. If user inputs the number which is equal to EXIT in the first place, print "No temperatures were entered"
3. If user inputs the number that is other than EXIT, then enter while loop to record max, min, average and
	the days of temperature which is lower than 16 degrees.
4. Print those four value out respectively. 

"""


EXIT = -100


def main():
	total = 0
	days = 0
	temper = int(input("Next temperature:(or " + str(EXIT) + " to quit): "))
	lowest = temper
	highest = temper
	if temper == EXIT:
		print("No temperatures were entered")
	while True:
		if temper == EXIT:
			break
		if temper >= highest:
			highest = temper
		if temper <= lowest:
			lowest = temper
		days += 1
		total += temper
		temper = int(input("Next temperature:(or " + str(EXIT) + " to quit): "))
	average = total / days
	print("高:" + str(highest))
	print("low:" + str(lowest))
	print("Average:" + str(average))
	print(str(days) + "cold days")



###### DO NOT EDIT CODE BELOW THIS LINE ######


if __name__ == "__main__":
	main()
