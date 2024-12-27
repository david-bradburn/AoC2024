#################################################################
###### https://adventofcode.com/2022/day/6 #######################
#################################################################
import numpy as np

file = "input.txt"

DAY_NO = "6"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

class pattern():
	def __init__(self, ip):
		self.clean_ip(ip)
		self.loop_position = 0
		for line_index in range(self.height):
			for item_index in range(self.width):
				print(item_index, line_index)
				self.clean_ip(ip)
				self.obstacle_map = self.obstacle_map_initial
				if self.obstacle_map[line_index][item_index] or (line_index == self.guard_loc_intial[1] and item_index == self.guard_loc_intial[0]):
					print("item/ guard already here")
					continue
				else:
					self.obstacle_map[line_index][item_index] = True # place obstacle
				
				self.guard_dir_map = self.guard_dir_map_initial
				self.guard_loc = self.guard_loc_intial
				self.guard_dir = self.guard_dir_initial
				self.guard_dir_map = np.zeros((self.height, self.width), dtype=str)
				self.guard_dir_map[self.guard_loc[1]][self.guard_loc[0]] = self.guard_dir
				# print(self.guard_dir_map)
				# print(self.guard_loc)
				# print(self.guard_dir)
				self.patrol()
		
		print(self.loop_position)

	def check_outsite_bounds(self, x, y):
		return x < 0 or y < 0 or x >= self.width or y >= self.height

	def return_tile_forward_clear(self, x, y):
		return not self.obstacle_map[y][x]

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
				print("Leaves area")
				break

			if self.return_tile_forward_clear(new_x, new_y):
				self.guard_loc = (new_x, new_y)

				if self.guard_dir in self.guard_dir_map[new_y][new_x]:
					# print(self.guard_dir, self.guard_dir_map[new_y][new_x])
					self.loop_position += 1
					print("Found")
					break
				else: 
					self.guard_dir_map[new_y][new_x] += self.guard_dir
			else:
				self.guard_turn()
				self.guard_dir_map[new_y][new_x] += self.guard_dir




	def clean_ip(self, ip):
		# print(rawInput)
		self.height = len(ip)
		self.width = len(ip[0].strip("\n"))

		
		self.obstacle_map = np.zeros((self.height, self.width), dtype=bool)
		self.obstacle_map_initial = np.zeros((self.height, self.width), dtype=bool)

		self.visited_map = np.zeros((self.height, self.width), dtype=bool)
		self.visited_map_initial = np.zeros((self.height, self.width), dtype=bool)

		self.guard_dir_map = np.zeros((self.height, self.width), dtype=str)
		self.guard_dir_map_initial = np.zeros((self.height, self.width), dtype=str)
		# print(self.guard_dir_map)
		self.guard_rep = ["^", ">", "v", "<"]
		for line_index, line in enumerate(rawInput):
			for item_index, item in enumerate(line.strip("\n")):
				if item == "#":
					self.obstacle_map[line_index][item_index] = True
					self.obstacle_map_initial[line_index][item_index] = True

				elif item in self.guard_rep:
					self.guard_loc = (item_index, line_index)
					self.guard_loc_intial = (item_index, line_index)
					self.visited_map[line_index][item_index] = True
					self.visited_map_initial[line_index][item_index] = True

					self.guard_dir = item
					self.guard_dir_initial = item
					self.guard_dir_map[line_index][item_index] = item
					self.guard_dir_map_initial[line_index][item_index] = item
				else:
					pass
		

p1  = pattern(rawInput)