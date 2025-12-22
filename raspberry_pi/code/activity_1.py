# create function to concatenate two strings in uppercase 


def conc_upp_str(str_a , str_b):
	new_str = str_a.upper() + " " + str_b.upper()
	return new_str
		
		
result = conc_upp_str("Hello" , "World")
print(result)
	
