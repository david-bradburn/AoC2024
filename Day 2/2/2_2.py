#################################################################
###### https://adventofcode.com/2022/day/2 #######################
#################################################################

file = "input.txt"

DAY_NO = "2"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

arr = []

for line in rawInput:
	tmp = line.strip("\n").split(" ")
	tmp_arr = [int(i) for i in tmp]
	arr.append(tmp_arr)

print(arr)


def inc_dec_only(arr: list) -> bool:
	inc_or_dec = 0
	for i in range(len(arr)):
		if i == 0:
			if arr[i+1] - arr[i] == 0:
				return False
			inc_or_dec = (arr[i+1] - arr[i])/abs(arr[i+1] - arr[i])
			print(inc_or_dec)
		else:
			delta = arr[i] - arr[i-1]
			abs_delta = abs(delta)

			if delta * inc_or_dec < 0 :
				return False
			if (abs_delta != 1) and (abs_delta != 2) and (abs_delta != 3):
				return False
	
	return True
		
total = 0
for line in arr:
	if inc_dec_only(line):
		total += 1
	else:
		for n in range(len(line)):
			tmptmp_arr = []
			for index, m in enumerate(line):
				if index != n:
					tmptmp_arr.append(m)
			
			if inc_dec_only(tmptmp_arr):
				total += 1
				break

	

print(total)