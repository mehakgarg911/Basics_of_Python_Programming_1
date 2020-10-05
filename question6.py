def reverse_list(list1):
	new_list=[]
	for x in list1:
		new_list = [x] + new_list
	return new_list

list1= [10,20,30,40,50]
print(reverse_list(list1))