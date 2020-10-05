import random
import string
from random import randint



def generate_pass():
	password = ""
	len_pass = randint(6,21)
	lower_letters = string.ascii_lowercase
	upper_letters = string.ascii_uppercase
	digits = string.digits
	special_char = string.punctuation

	password+=random.choice(lower_letters)    #atleast 1 lowercase character
	password+=random.choice(upper_letters)    #atleast 1 uppercase character
	password+=random.choice(digits)           #atleast 1 digit
	password+=random.choice(special_char)     #only 1 special character
	random_all = lower_letters + upper_letters + digits

	for x in range(4,len_pass):
		password+=random.choice(random_all)
	shuffled_pass = ''.join(random.sample(password,len_pass))
	return shuffled_pass

print(generate_pass())


	

