
def obtenir_choix_utilisateur():
    while True:
        choix_utilisateur_str = input("quel est votre choix: ")
        try:
            choix_utilisateur_int =int(choix_utilisateur_str)
            if choix_utilisateur_int in [1,2,3]:
                return choix_utilisateur_int
            else:
                print("Merci de choisir un entier parmis 1, 2 ou 3")
                obtenir_choix_utilisateur()
        except:
            print("Merci d'entrée un entier")
            obtenir_choix_utilisateur()


result=obtenir_choix_utilisateur()

print(result)
