def pattern(num1):

	for x in range(1,num1):
		for i in range(x):
			print("*",end =" ")
		print("\n")

	for x in range(num1,0,-1):
		for i in range(x):
			print("*",end =" ")
		print("\n")


pattern(4)