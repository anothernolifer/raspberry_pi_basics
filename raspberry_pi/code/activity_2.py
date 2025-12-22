# validate user input for a number between 1 and 100

number = int(input("Enter a number between 1 and 100: "))

if number <=0 or number > 100:
	print("Error: Number out of range." + str(number))
	
else:
    print("Number accepted: " + str(number))