# compute the maximum value in a list of numbers


def find_maximum(number_list):
    max_value = 0
    for number in number_list:
        if number > max_value:
            max_value = number
    return max_value

number_list = [3, 5, 78, -7, 45]
max_value = find_maximum(number_list)

print("The maximum value is:" + str(max_value))
