"""
File: caesar.py
Name: Lina Chou
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
"""
流程:
1. 請使用者入須右移的次數及要解開的密碼
2. 將輸入字母轉成大寫
3. 藉由重組字串得出右移後的字母排序,稱新字串
4. 當輸入字串等於新字串時,找出index值,再比照原Alphabet字串中的index,得出解密字串;若輸入值非字母,則照原本輸入的呈現ex: ! ?
5. 印出解密字串

Process:
1. Let user input how many times Alphabet would move to the right and the password.
2. Turn it into uppercase letters.
3. Get new alphabet oder by reorganize it.
4. To decrypt, finding the index of new string when inputting alphabet is same as new string's.
    If inputting value is not alphabet then get what it was.
5. Print the decoded string.
"""


def main():
    secret_num = int(input("Secret number: "))  # 向右平移格數
    solve = input("What's the ciphered string?")
    new_solve = solve.upper()
    ans = ""
    for i in range(0, len(ALPHABET)-secret_num):
        ch = ALPHABET[i]
        ans += ch
    ans = ALPHABET[len(ALPHABET)-secret_num:] + ans  # reassign ans,將由A開頭的字串,新排序在所有字母後面
    ans2 = ""
    for k in range(len(solve)):
        for j in range(len(ALPHABET)):  # 26個字母 26次迴圈
            if new_solve[k] == ans[j]:  # 當輸入字串等於右移後的字母
                ans2 += ALPHABET[j]
        if not new_solve[k].isalpha():  # 當輸入字串不是字母
            ans2 += new_solve[k]
    print(ans2)




#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
