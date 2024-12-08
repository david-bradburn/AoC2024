#################################################################
###### https://adventofcode.com/2022/day/4 #######################
#################################################################

import numpy as np


file = "input.txt"

DAY_NO = "4"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

print(rawInput)
# Need to process the array

class WordSearch():
	def __init__(self, data):
		self.ip = data
		self.height = len(self.ip)
		self.width = len(self.ip[0].strip("\n"))

		self.board = np.empty((self.height, self.width), dtype=str)
		self.load_data()
		self.total = 0
		self.search_next_letter()

		print(f"Total: {self.total}")
	
	def return_count_xmas(self, index: tuple):
		delta = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
		list_of_words = []
		for direction in delta:
			x, y = index
			val = "X"
			# print(f" delta {direction}")
			for i in range(3):
				x += direction[0]
				y += direction[1]
				# print(x, y)

				if abs(x) != x or abs(y) != y:
					break
				try: 
					val += self.board[y][x]
				
				except IndexError:
					break

			list_of_words.append(val)

		# print(list_of_words)
		tmp_count = 0
		for word in list_of_words:
			if word == "XMAS":
				tmp_count += 1
		return tmp_count

	def search_next_letter(self):
		total_Xs = 0
		for line_index, line in enumerate(self.board): #y
			for item_index, item in enumerate(line): #x
				if item == "X":
					# print(item_index, line_index)
					total_Xs += 1
					self.total += self.return_count_xmas((item_index, line_index))

		# print(f"number of X's {total_Xs}")

	def load_data(self):
		for line_index, line in enumerate(self.ip):
			clean_line =  line.strip("\n")
			for item_index, item in enumerate(clean_line):
				self.board[line_index][item_index] = item
		print(self.board)

p1 = WordSearch(rawInput)
			
			