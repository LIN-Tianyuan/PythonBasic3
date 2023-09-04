number = [32, 5, 12, 8, 3, 75, 2, 15]
number_a = 0
for number_b in range(len(number)):
    for number_c in range(len(number)):
        if number[number_c] > number[number_a]:
            number_a = number_a + 1
            result = number[number_c]
            print(result)