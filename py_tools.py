import datetime as dt

print("""Hello from py_tools! 
If you like py_tools then make sure to star it. 
If you find any issues then report it at https://github.com/Platformer444/py_tools/isses .""")

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
def Get_Index_Of_Item_In_List(listSpecified, Item):
	for i in range(len(listSpecified)):
		if str(listSpecified[int(i)]) == str(Item):
			print(i)

# Finds the average/mean of numbers
def Average_Of(numbers):
	num = 0
	for i in range(len(numbers)):
		num = num + int(numbers[int(i)])
	print(num/len(numbers))

# Print the current date and time
def Print_Date_And_Time():
	d_t = dt.datetime.now()
	Date = d_t.strftime('%d') + '-' + d_t.strftime('%m') + '-' + d_t.strftime('%Y')
	print(Date)
	Time = d_t.strftime('%I') + ':' + d_t.strftime('%M') + ':' + d_t.strftime('%S') + ' ' + d_t.strftime('%p')
	print(Time)
