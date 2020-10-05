def factorial(num1):
	fact =1
	for x in range(2,num1+1):
		fact*=x
	return fact

def rec_factorial(num1):
	if num1==0 or num1==1:
		return 1;
	else:
	    return num1*rec_factorial(num1-1);

print(factorial(6))
print(rec_factorial(6))