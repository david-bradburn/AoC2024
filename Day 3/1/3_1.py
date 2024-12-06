#################################################################
###### https://adventofcode.com/2022/day/3 #######################
#################################################################

import re

file = "input.txt"

DAY_NO = "3"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

total = 0

print(rawInput[0])
for i in rawInput:
	x = re.findall("mul\([0-9]*,[0-9]*\)", i)

	for mul in x:
		tmp = mul.lstrip("mul(").rstrip(")").split(",")
		x, y = int(tmp[0]), int(tmp[1])
		total += x*y

print(total)
