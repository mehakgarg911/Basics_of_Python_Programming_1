def find_occurance(str1,text1):
	str1=str1.lower()
	text1=text1.lower()
	len1=len(str1)
	len2=len(text1)
	count=0
	for x in range(len1-len2):
		if(str1[x:x+len2]==text1):
			count+=1;
	return count;


str1 = "Welcome to USA. usa awesome, isn't it?"
print(find_occurance(str1,"USA"))