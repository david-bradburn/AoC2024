#################################################################
###### https://adventofcode.com/2022/day/3 #######################
#################################################################

import re

file = "input.txt"

DAY_NO = "3"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

def strip_return_prod(ip: str) -> int:
		tmp = ip.lstrip("mul(").rstrip(")").split(",")
		x, y = int(tmp[0]), int(tmp[1])
		return x*y
		# return total

# def add_to_dict(lis: list):
# 	tmp_dict

def return_match(pattern, ip):#
	tmp = {}
	for tmp_n in re.finditer(pattern, ip):
		tmp[tmp_n.start()] = tmp_n.group(0)
	print(tmp)
	return tmp
print(rawInput[0])

enable = True
total = 0

def check_type(ip):
	if len(ip) == 4:
		return 1
	elif len(ip) == 7:
		return 0
	else:
		return 2

for i in rawInput:
	# process each line
	tmpLine = return_match("mul\([0-9]*,[0-9]*\)", i)
	tmpLine.update(return_match("do\(\)", i))
	tmpLine.update(return_match("don't\(\)", i))
	sortedtmp = dict(sorted(tmpLine.items()))
	
	for key in sortedtmp:
		result = check_type(sortedtmp[key])
		if result == 1:
			enable = True
		elif result == 0:
			enable = False
		else:
			if enable:
				total += strip_return_prod(sortedtmp[key])

			
print(total)
