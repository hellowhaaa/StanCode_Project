"""
File: similarity.py
Name: Lina Chou
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""

"""
main 流程:
1.請使用者輸入一基因序列及欲尋找之序列
2.將兩者皆轉為大寫字母
3.利用function 'find' 將最相似字串找出
4.印出字串

Process of main:
1. Let user input a DNA sequence and the sequence that user wanna search.
2. Turn both them into uppercase letters.
3. Utilize function 'find' to find the most similar string from DNA sequence.
4. Print it out.
"""


def main():
    all_dna = input("Please give me a DNA sequence to search: ")
    wants = input("What DNA sequence would you like to match? ")
    new_all = all_dna.upper()
    new_wants = wants.upper()
    s = find(new_all, new_wants)
    print("The beast match is " + s)


def find(long, short):

    """
    用途:找出相似字串
    流程:欲尋找的短基因序列的index是固定的,而長基因序列的index會隨著迴圈增加,
    其序列長度由短基因的長度決定,直到兩者配對到最後一個字母,藉由紀錄最高值找出相似度最高的序列
    Purpose: Find the most similar string.
    Process: The index of short DNA string is fixed. However,The index of short DNA string
             increases while in loop. The length of each string are determined by short string.
             The function won't end until the last alphabet is executed.
    """
    letters = ""  # 欲尋找的相似基因片段
    times = 0  # 相同字母的次數
    highest = 0
    for k in range(0, len(long)-len(short)+1):  # 長基因序列index往右移
        times = 0
        ch1 = long[k:k + len(short)]  # 長基因的字串
        ch = short[0:len(short)]  # 短基因的字串
        for j in range(0, len(short)):
            s1 = ch1[j]
            s2 = ch[j]
            if s1 == s2:
                times += 1
            if times > highest:
                highest = times  # highest越高表字串相似度越高
                letters = long[k:k + len(short)]  # 相似度最高的字串
    return letters







###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
