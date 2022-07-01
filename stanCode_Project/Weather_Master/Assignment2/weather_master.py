"""
File: weather_master.py
Name: Lina Chou
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
	print("stanCode \"Weather Master 4.0\"!")
	tem = int(input("Next Temperature: (or "+str(EXIT)+" to quit)?"))
	if tem == EXIT:
		print("No temperatures were entered.")
	else:
		cold_day = 0  # 設低於16度以下的天數初始為0
		highest = tem  # 最高溫(最大值)
		lowest = tem  # 最低溫(最小值)
		times = 0  # 設迴圈次數初始為0
		tem_total = 0  # 設溫度加總初始為0
		while tem != EXIT:  # 若使用者未輸入EXIT數值則持續迴圈
			tem_total += tem  # 加總使用者輸入的數值
			times += 1  # 迴圈次數加一
			if tem < 16:  # 若輸入值低於16,則記錄次數
				cold_day += 1
			if tem > highest:  # 若輸入值大於目前最大值,則assign新輸入的值為最大值
				highest = tem
			if tem < lowest:  # 若輸入值小於目前最小值,則assign新輸入的值為最小值
				lowest = tem
			tem = int(input("Next Temperature: (or " + str(EXIT) + " to quit)?"))
		average = tem_total / times  # 使加總值除以迴圈次數計算平均值
		print("Highest temperature = " + str(highest))
		print("Lowest temperature = " + str(lowest))
		print("Average = "+str(average))
		print(str(cold_day) + " cold day(s)")


if __name__ == "__main__":
	main()
