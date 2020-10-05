
def input_list():
	list1 = []
	for x in range(1,6):
		print("Enter number {}:".format(x))
		list1.append(float(input()))

	return list1

print(input_list())