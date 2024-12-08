#################################################################
###### https://adventofcode.com/2022/day/4 #######################
#################################################################

import numpy as np


file = "input.txt"

DAY_NO = "4"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

# print(rawInput)
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
	
	def check_out_bounds(self, coord: tuple):
		x,y = coord
		return (abs(x) != x or abs(y) != y) or x >= self.width or y >= self.height
	
		
	def return_count_x_mas(self, index: tuple):
		delta = [(1, 1), (-1, 1)]
		for direction in delta:
			x, y = index
			val = "X"

			x_d1 = x + direction[0]
			y_d1 = y + direction[1]
			x_d2 = x - direction[0]
			y_d2 = y - direction[1]
		
			if self.check_out_bounds((x_d1, y_d1)) or self.check_out_bounds((x_d2, y_d2)):
				return 0

			val_d1 = self.board[y_d1][x_d1]
			val_d2 = self.board[y_d2][x_d2]

			either_S = (val_d1 == "S") or (val_d2 == "S")
			either_M = (val_d1 == "M") or (val_d2 == "M")

			SandM = either_S and either_M

			if not SandM:
				return 0

		return 1

	def search_next_letter(self):
		for line_index, line in enumerate(self.board): #y
			for item_index, item in enumerate(line): #x
				if item == "A":
					# print(item_index, line_index)
					self.total += self.return_count_x_mas((item_index, line_index))

		# print(f"number of X's {total_Xs}")

	def load_data(self):
		for line_index, line in enumerate(self.ip):
			clean_line =  line.strip("\n")
			for item_index, item in enumerate(clean_line):
				self.board[line_index][item_index] = item
		print(self.board)

p1 = WordSearch(rawInput)
			
			