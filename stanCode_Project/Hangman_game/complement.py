"""
File: complement.py
Name: Lina Chou
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""

"""
流程:
1.請使用者輸入一段基因序列
2.將序列轉為大寫
3.印出相對應的英文字母

Process:
1. Let user input a DNA sequence.
2. Turn it into uppercase letters.
3. Print letters that respond to each inputting letter.
"""


def main():
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    big_dna = dna.upper()
    t = build_complement(big_dna)
    print("The complement of " + big_dna + " is " + t)


def build_complement(big_dna):
    ans = ""
    for ch in big_dna:
        if ch == "A":
            ans += "T"
        elif ch == "T":
            ans += "A"
        elif ch == "C":
            ans += "G"
        elif ch == "G":
            ans += "C"
    return ans






###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
