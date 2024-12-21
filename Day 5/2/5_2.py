#################################################################
###### https://adventofcode.com/2022/day/5 #######################
#################################################################

import re

typefile = "input"


file1 = typefile + "_instr.txt"
file2 = typefile + "_data.txt"

DAY_NO = "5"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file1, "r") as fd:
	rawInputInstr = fd.readlines()

with open(file_path_base + file2, "r") as fd:
	rawInputData = fd.readlines()

class Safety():

	def matchInstr(self, book):
		matchedInstr = []
		for instrPair in self.instr:
			if instrPair[0] in book and instrPair[1] in book:
				matchedInstr.append(instrPair)
			
		return matchedInstr

	def countMidBook(self, list_of_books):
		self.total = 0
		for book in list_of_books:
			mid = int((len(book) - 1)/2)
			print(book[mid])
			self.total += book[mid]

	
	def findInvalidBooks(self):
		self.invalidBooks = []
		for book in self.data:
			matchingInstr = self.matchInstr(book)

			for instr in matchingInstr:
				if re.search(f"{instr[0]},.*{instr[1]}", str(book)) == None:
					print(f"Found invalid book: {book}")
					self.invalidBooks.append(book)
					break

	def checkBook(self, book):
		matchingInstr = self.matchInstr(book)
		for instr in matchingInstr:
			if re.search(f"{instr[0]},.*{instr[1]}", str(book)) == None:
				return True

		return False

	def sortBook(self):
		self.sortedBooks= []
		for book in self.invalidBooks:
			matchingInstr = self.matchInstr(book)
			unsorted = True
			while unsorted:
				for instr in matchingInstr:
					if re.search(f"{instr[0]},.*{instr[1]}", str(book)) != None:
						continue
					else:
						# instruction doesn't match
						indexInstr0 = book.index(instr[0])
						book.pop(book.index(instr[1]))
						book.insert(indexInstr0, instr[1])

				unsorted = self.checkBook(book)
			self.sortedBooks.append(book)
		# print(self.sortedBooks)
			


	def __init__(self, instr, data):
		self.clean(instr, data)
		self.findInvalidBooks()
		self.sortBook()
		self.countMidBook(self.sortedBooks)
		print(self.total)
		

	def clean(self, instr, data):
		self.instr = []
		self.data = []
		for line in instr:
			clean_line = line.strip()
			pair = clean_line.split("|")
			# print(pair)
			self.instr.append([int(pair[0]), int(pair[1])])
		
		for line in data:
			clean_line = line.strip()
			book = clean_line.split(",")
			temp = []
			for page in book:
				temp.append(int(page))
			# print(temp)
			self.data.append(temp)
		
p1 =  Safety(rawInputInstr, rawInputData)

			
		


