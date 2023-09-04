import random
number_a = random.randint(1, 100)
for indicator in range(1, 99999999):
    number_b = int(input("Entrer votre nombre: "))
    if number_b == number_a:
        if indicator == 1:
            print("Incroyble, vous avez trouver dans le premier coup.")
        else:
            print("Bravo, vous avez pris " + str(indicator) + " d'essai pour trouver le bon nombre.")
        break
    elif number_b > 100:
        print("Nombre incorrect.")
    else:
        if number_b > number_a:
            print("C'est moins.")
        else:
            print("C'est plus.")
