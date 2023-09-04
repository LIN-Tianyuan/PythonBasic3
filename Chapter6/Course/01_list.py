# Création d'une liste
leisure = ['swim', 'dance', 'sing']
print(leisure)          # ['swim', 'dance', 'sing']
# Longueur d'une liste
print(len(leisure))     # 3
# Test de présence d'un élément
print("basketball" in leisure)  # False
print('dance' in leisure)   # True
print('DANCE' in leisure)   # False
# Index d'un élément
print(leisure.index("swim"))    # 0
# Accéder aux éléments d'une liste
print(leisure[1])   # dance
# Modifier la valeur d'un élément de liste
leisure[0] = "ski"
print(leisure)  # ['ski', 'dance', 'sing']
# Ajouter un élément à une liste
leisure.append("game")
print(leisure)
# Insérer un élément ailleurs qu'à la fin
# leisure.insert(3, "climb")
# print(leisure)
leisure.insert(leisure.index("game"), "climb")
print(leisure)  # ['ski', 'dance', 'sing', 'climb', 'game']
# Enlever un élément de liste
leisure.remove("climb")
print(leisure)  # ['ski', 'dance', 'sing', 'game']
# Enlever un élément ailleurs avec son index
leisure.pop(1)
print(leisure)  # ['ski', 'sing', 'game']
# Vider une liste
leisure.clear()
print(leisure)  # []

print("----------")
# Concaténer deux listes
month = ['Janvier', 'Février', 'Mars']
season = ['Automne', 'Hiver', 'Printemps', 'Eté']
various_times = month + season
print(various_times)    # ['Janvier', 'Février', 'Mars', 'Automne', 'Hiver', 'Printemps', 'Eté']
# Etendre une liste
month.extend(season)
print(month)    # ['Janvier', 'Février', 'Mars', 'Automne', 'Hiver', 'Printemps', 'Eté']
print(season)   # ['Automne', 'Hiver', 'Printemps', 'Eté']

print("----------")
# Créer une tranche de liste
rainbow = ['rouge', 'orange', 'jaune', 'vert', 'bleu', 'indigo', 'violet']
print(len(rainbow))     # 7
print(rainbow[1:4])     # ['orange', 'jaune', 'vert']
print(rainbow[3:])      # ['vert', 'bleu', 'indigo', 'violet']
print(rainbow[:5])      # ['rouge', 'orange', 'jaune', 'vert', 'bleu']
print(rainbow[-5:-2])   # ['jaune', 'vert', 'bleu']
