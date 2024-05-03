def welcome():
    name_visitor = input("Merci de contacter Thibault ! Je peux avoir votre prénom? ")
    print("Bienvenue chez Thibault! " + name_visitor)
    return


def choose_categ():
    print("*** Menu général Thibault ***\n"
          "[1] Horaires & Accès\n"
          "[2] Gestion de commande\n"
          "[3] Suivi de livarison\n"
          "[4] Suggestion de produit\n"
          "[5] Autre sujet")
    c_catego = int(input("Choisissez une des catégories en tapant un chiffre entre 1 et 5: "))
    if c_catego == 1:
        # Horaires & Accès
        shop_info()
        return
    elif c_catego == 2:
        # Gestion de commande
        order_management()
        return
    elif c_catego == 3:
        # Suivi de livarison
        tracking_deliveries()
        return
    elif c_catego == 4:
        # Suggestion de produit
        service_marketing()
        return
    elif c_catego == 5:
        # Autre sujet
        others()
        return
    else:
        choose_categ()
        return


def shop_info():
    address = "148 Boulevard Masséna 75013 PARIS"
    schedule = 'du Lundi au Samedi 10h-18h'
    print("Thibault se retrouve au " + address + ".\nLa boutique est ouverte " + schedule + ".")
    other = input("Autre chose?[y/n]")
    if other == 'y':
        choose_categ()
    else:
        print("Merci de nous avoir contacté.")
    return


def order_management():
    print("\nVous êtes au service de gestion des commandes.")
    client_name = input("Nom indiqué sur le bon de commande: ")
    order_number = input("Indiquez le numéro de commande: ")
    transfer_Elliot()
    return


def transfer_Christine():
    print("Merci pour vos détails. Nous vérifions votre commande et vous recontactons au plus vite.")
    return


def tracking_deliveries():
    print("Nous sommes désolés que vous ayez subi un souci avec votre commande.")
    client_name = input("Nom indiqué sur le bon de commande: ")
    order_number = input("Indiquez le numéro de commande: ")
    follow = input("Décrivez votre problème: ")
    transfer_Christine()
    return


def transfer_Raoul():
    suggestion_marketing = input("Dites-moi quel autre produit nous devrions proposer: ")
    return

def transfer_Therese():
    other_info = input("De quoi aimeriez-vous nous informer? ")
    return


def service_marketing():
    print("Nous vous remercions pour votre suggestion et allons vous mettre en relation avec le service concerné.")
    transfer_Raoul()
    return

def transfer_Elliot():
    print("Parfait! Je vérifie le statut de votre commande.")
    return



def others():
    transfer_Therese()
    return



welcome()
choose_categ()