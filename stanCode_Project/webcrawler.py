"""
File: webcrawler.py
Name: Lina Chou
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        male_total = 0
        female_total = 0
        tags = soup.find_all({'tbody': 'tr'})
        for tag in tags:
            a = tag.text
            each_year_list = a.split()
            for j in range(200):  # 200筆資料
                specific_num = each_year_list[2+5*j]
                new_string1 = ""
                for i in range(len(specific_num)):  # 重新串字串,將","去除掉
                    ch = specific_num[i]
                    if ch != ',':
                        new_string1 += ch
                male_total += int(new_string1)
                specific_num2 = each_year_list[4+5*j]
                new_string2 = ""
                for k in range(len(specific_num2)):  # 重新串字串,將","去除掉
                    ch2 = specific_num2[k]
                    if ch2 != ',':
                        new_string2 += ch2
                female_total += int(new_string2)
            print('Male Number: ' + str(male_total))
            print('Female Number: ' + str(female_total))


if __name__ == '__main__':
    main()
