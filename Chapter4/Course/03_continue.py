# Imprimez les nombres pairs entre 2 et 10, sauf 8
num = 0
while num < 10:
    num = num + 2
    if num == 8:
        continue
    print(num)