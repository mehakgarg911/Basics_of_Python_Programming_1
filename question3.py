def middle_str(str1):
	len1=len(str1)
	a=(len1//2)-1;
	mid = str1[a:a+3]
	return mid;

str1="JaSonAy"
print(middle_str(str1))