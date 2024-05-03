number_list = [32, 5, 12, 8, 3, 75, 2, 15]
max_num = number_list[0]
for number in number_list:
    if max_num <= number:
        max_num = number
print("Le plus grand élément de cette liste est la valeur: " + str(max_num) + ".")
