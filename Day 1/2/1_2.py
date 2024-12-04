#################################################################
###### https://adventofcode.com/2022/day/1 #######################
#################################################################

file = "input.txt"

DAY_NO = "1"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

list_left = []
list_right = []
## I want to split into 2 lists

for element in rawInput:
	pair = element.strip("\n").split("   ")
	list_left.append(int(pair[0]))
	list_right.append(int(pair[1]))
list_left.sort()
list_right.sort()

assert len(list_right) == len(list_left)

def find_count_in_list(num, arr):
	count = 0
	for element in arr:
		if num == element:
			count += 1
	return count

total = 0
for ele in list_left:
	total += ele * find_count_in_list(ele, list_right)

print(total)