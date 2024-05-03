a = int(input("Veuillez entrer une année: "))
if a % 4 == 0 and a % 100 != 0:
    print(str(a) + " est une année bissextile.")
elif a % 400 == 0 and a % 100 == 0:
    print(str(a) + " est une année bissextile.")
else:
    print(str(a) + " n'est pas une année bissextile.")