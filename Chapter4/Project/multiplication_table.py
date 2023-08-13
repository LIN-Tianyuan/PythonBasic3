for number_a in range(1, 10):
    for number_b in range(1, number_a+1):
        print("%d * %d = %d " %(number_a, number_b, number_a * number_b), end="\t")
    print()
