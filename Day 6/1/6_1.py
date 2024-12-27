#################################################################
###### https://adventofcode.com/2022/day/6 #######################
#################################################################
import numpy as np

file = "input.txt"

DAY_NO = "6"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

class pattern():
	def __init__(self, ip):
		self.clean_ip(ip)
		self.patrol()
		self.count_visited_tiles()

	def check_outsite_bounds(self, x, y):
		return x < 0 or y < 0 or x >= self.width or y >= self.height

	def return_tile_forward_clear(self, x, y):
		return not self.obstacle_map[y][x]
	
	def count_visited_tiles(self):
		self.total = 0
		for line in self.visited_map:
			for item in line:
				self.total += int(item)
		
		print(self.total)

	def guard_turn(self):
		indexdir = self.guard_rep.index(self.guard_dir)

		if indexdir < len(self.guard_rep) - 1:
			self.guard_dir = self.guard_rep[indexdir + 1]
		else:
			self.guard_dir = self.guard_rep[0]

	def patrol(self):
		while True:
			match(self.guard_dir):
				case "^":
					new_x = self.guard_loc[0] 
					new_y = self.guard_loc[1] - 1
				case ">":
					new_x = self.guard_loc[0] + 1
					new_y = self.guard_loc[1]
				case "v":
					new_x = self.guard_loc[0] 
					new_y = self.guard_loc[1] + 1
				case "<":
					new_x = self.guard_loc[0] - 1
					new_y = self.guard_loc[1]

				case _:
					raise Exception
			if self.check_outsite_bounds(new_x, new_y):
				break
			if self.return_tile_forward_clear(new_x, new_y):
				self.guard_loc = (new_x, new_y)
				self.visited_map[new_y][new_x] = True
			else:
				self.guard_turn()




	def clean_ip(self, ip):
		print(rawInput)
		self.height = len(ip)
		self.width = len(ip[0].strip("\n"))

		
		self.obstacle_map = np.zeros((self.height, self.width), dtype=bool)
		self.visited_map = np.zeros((self.height, self.width), dtype=bool)
		self.guard_rep = ["^", ">", "v", "<"]
		for line_index, line in enumerate(rawInput):
			for item_index, item in enumerate(line.strip("\n")):
				if item == "#":
					self.obstacle_map[line_index][item_index] = True
				elif item in self.guard_rep:
					self.guard_loc = (item_index, line_index)
					self.visited_map[line_index][item_index] = True
					self.guard_dir = item
				else:
					pass
		

p1  = pattern(rawInput)