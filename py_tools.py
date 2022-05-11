# Doing some arithmetic operation with the nmbers in the specified list
def Arithmetic_Operation_With_Lists(listToBeCalculated, Operation):
	num = 0
	for i in range(len(listToBeCalculated)):
		if Operation == "+":
			num = int(listToBeCalculated[int(i)]) + num
		elif Operation == "-":
			if num == 0:
				num = int(listToBeCalculated[int(i)]) + num
			else:
				num = num - int(listToBeCalculated[int(i)])
		elif Operation == "*":
			if num == 0:
				num = int(listToBeCalculated[int(i)]) + num
			else:
				num = int(listToBeCalculated[int(i)]) * num
		elif Operation == "/":
			if num == 0:
				num = int(listToBeCalculated[int(i)]) + num
			else:
				num = num / int(listToBeCalculated[int(i)])
	print(num)

# Join All The Contents in a list
def Join_Everything_In_List(listToBeJoined):
	Result = ''
	for i in range(len(listToBeJoined)):
		Result = Result + str(listToBeJoined[int(i)])
	print(Result)

# Get the index of a item in a list
def Get_Index_Of_A_Character_In_List(listSpecified, Item):
	for i in range(len(listSpecified)):
		if str(listSpecified[int(i)]) == str(Item):
			print(i)