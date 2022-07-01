"""
File: boggle.py
Name: Lina Chou
----------------------------------------
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	When the user inputs 4*4 boggle board, this program will find all boggle answers.
	"""

	rows = []
	for i in range(4):
		while True:
			letters = input(str(i+1) + ' row of letters: ')
			letters = letters.lower()
			line_lst = letters.strip().split()

			valid_input = True
			if len(line_lst) != 4:
				print('Illegal input')
				valid_input = False
			else:
				for ch in line_lst:
					if not ch.isalpha() or len(ch) != 1:
						print('Illegal input')
						valid_input = False
						break
			if valid_input:
				rows.append(line_lst)
				break
	start = time.time()
	####################
	ans = find_word(rows)
	print('There are ' + str(len(ans)) + ' words in total.')
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	info = {}
	with open(FILE, 'r') as f:
		for line in f:
			line = line.strip()
			ch = line[0]
			if ch not in info:  # 將單字的字母開頭存成 key value
				info[ch] = [line]
			else:
				info[ch].append(line)
	return info


def has_prefix(sub_s, info):
	"""
	:param info: dict
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in range(len(info[sub_s[0]])):
		if info[sub_s[0]][i].startswith(sub_s):
			return True
	return False


def find_word(s):
	"""
	:param s:(list) The boggle board to be used.
	:return boggle_answer: (list) The list used to store all found boggle answers.
	"""

	dic = read_dictionary()
	boggle_answer = []
	for y in range(4):
		for x in range(4):
			# 座標(0, 0) --> (3, 3)
			index = []
			cur_s = ""
			cur_s += s[y][x]
			index.append((y, x))
			boggle_answer = find_word_helper(s, index, dic, y, x, cur_s, boggle_answer)
	return boggle_answer


def find_word_helper(s, index, dic, y, x, current_s, boggle_answer):
	"""
	:param s:(list) The boggle board to be used.
	:param index: (list) Stores all the chosen characters' position.
	:param dic:(dic) The dictionary has been categorized by each word's first letter and stores all English vocabularies.
	:param y: (int) The position of the point with reference to the y-axis.
	:param x: (int) The position of the point with reference to the x-axis.
	:param current_s:(str) Concatenates all characters that have been chosen.
	:param boggle_answer: (list) The list used to store all found boggle answers.
	"""

	if len(current_s) >= 4:
		if current_s not in boggle_answer:
			if current_s in dic[current_s[0]]:
				boggle_answer.append(current_s)
				print('Found ' + current_s)
	for j in range(y-1, y+2):
		for i in range(x-1, x+2):
			if 0 <= i <= 3 and 0 <= j <= 3:
				if (j, i) not in index:
					# Choose
					index.append((j, i))
					current_s += s[j][i]
					# Explore
					if has_prefix(current_s, dic):
						find_word_helper(s, index, dic, j, i, current_s, boggle_answer)
					# Un-choose
					index.pop()
					current_s = current_s[:-1]
	return boggle_answer


if __name__ == '__main__':
	main()
