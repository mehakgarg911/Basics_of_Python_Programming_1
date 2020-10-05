def mixed_string(str1,str2):
    str_mixed = ""
    len1 =len(str1)
    len2 =len(str2)
    str2 = str2[::-1]
    if len1>len2:
	    for x in range(len2):
	        str_mixed+=str1[x]
	        str_mixed+=str2[x]
	    for y in range(len2,len1):
	    	str_mixed+=str1[y]
    else:
        for x in range(len1):
	        str_mixed+=str1[x]
	        str_mixed+=str2[x]
        for y in range(len1,len2):
	        str_mixed+=str2[y]

    return str_mixed
        
str1 = 'Abc'
str2 = 'Xyz'
print(mixed_string(str1,str2))