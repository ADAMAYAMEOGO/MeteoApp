import datetime
import os
from meteo_utils import *
import couleur

# constantes spécifiques au module pour le formatage à l'écran sous forme de tableau
ECRAN_NOMBRE_COLONNES = 200
DESCRIPTION_NOMBRE_COLONNES = 20
JOUR_NOMBRE_COLONNES = 25


def _fermer_ligne(message):
    """
    permet de clôturer une ligne de texte avec le caractère "|" en le positionnant à une position qui respecte la taille
    du tableau graphique souhaité (afin d'obtenir un effet visuel de cadre pour le tableau souhaité)
    :param message: le texte à affiché sur la ligne
    :return: le message + les espaces nécessaire + le caractère "|" qui ferme visuellement la ligne
    """
    nombre_caractere_ajout = ECRAN_NOMBRE_COLONNES - 2 - len(message)  # (80 colonnes - la fermeture de ligne)
    chaine_complement = " " * nombre_caractere_ajout + "|"
    return message + chaine_complement


def _fermer_section(message, taille_section, caractere_fin_destion):
    """
    Une section est une zone du tableau, ici clôturée par le caractère proposé en paramètre, en fonction de la taille de la section souhaitée
    :param message: le texte à afficher
    :param taille_section: la taille de la section souhaité (en nombre de caracères)
    :param caractere_fin_destion: le caractère de clôture de section souhaité
    :return: la chaine de caractère formatée avec le caractère de clôture
    """
    nombre_caractere_ajout = taille_section - 1 - len(message)
    chaine_complement = " " * nombre_caractere_ajout + caractere_fin_destion
    return message + chaine_complement


def _afficher_ligne_prevision(text, val_jour1, val_jour2, val_jour3, val_jour4, val_jour5, val_jour6, val_jour7):
    """
    formatage des données pour créer une ligne d'affichage pour les prévisions météo
    :param text: la description du type de prévision affiché
    :param val_jour1: la valeur pour le jour prévu
    :param val_jour2: la valeur pour le jour prévu
    :param val_jour3: la valeur pour le jour prévu
    :param val_jour4: la valeur pour le jour prévu
    :param val_jour5: la valeur pour le jour prévu
    :param val_jour6: la valeur pour le jour prévu
    :param val_jour7: la valeur pour le jour prévu
    """
    description = _fermer_section("| " + text, DESCRIPTION_NOMBRE_COLONNES, '|')
    jour1 = _fermer_section(" " + str(val_jour1), JOUR_NOMBRE_COLONNES, '|')
    jour2 = _fermer_section(" " + str(val_jour2), JOUR_NOMBRE_COLONNES, '|')
    jour3 = _fermer_section(" " + str(val_jour3), JOUR_NOMBRE_COLONNES, '|')
    jour4 = _fermer_section(" " + str(val_jour4), JOUR_NOMBRE_COLONNES, '|')
    jour5 = _fermer_section(" " + str(val_jour5), JOUR_NOMBRE_COLONNES, '|')
    jour6 = _fermer_section(" " + str(val_jour6), JOUR_NOMBRE_COLONNES, '|')
    jour7 = _fermer_section(" " + str(val_jour7), JOUR_NOMBRE_COLONNES, '|')

    print(description + jour1 + jour2 + jour3 + jour4 + jour5 + jour6 + jour7)


def afficher_en_tete(ville, temperature, condition_meteo):
    """
    Formatage de l'en tête contenant les informations de météo actuelle pour une ville donnée
    :param ville: la ville sur laquelle porte la recherche
    :param temperature: la température actuelle
    :param condition_meteo: une description courte de la condition météo actuelle
    """
    message1 = "Ville: " + ville
    message2 = "Temperature: " + str(temperature)
    message3 = "Condition: " + condition_meteo
    message_ligne = _fermer_ligne("| " + message1 + " > " + message2 + " > " + message3)
    print("|" + ("-" * (ECRAN_NOMBRE_COLONNES - 7)) + "|")
    print(f"{couleur.BOLD} {message_ligne} {couleur.RESET}")
    print("|" + ("-" * (ECRAN_NOMBRE_COLONNES - 7)) + "|")


def afficher_previsions(previsions):
    """
    Formatage et affichage des prévisions avec les jours de la semaine en colonne et pour chaque ligne
    un type de prévision différents (en fonction de la liste des privisions passée en paramètre
    :param previsions: listes des prévisions (lignes préformatées en mémoire)
    """
    j_1 = get_jour(PREVISION_J_PLUS_1)
    j_2 = get_jour(PREVISION_J_PLUS_2)
    j_3 = get_jour(PREVISION_J_PLUS_3)
    j_4 = get_jour(PREVISION_J_PLUS_4)
    j_5 = get_jour(PREVISION_J_PLUS_5)
    j_6 = get_jour(PREVISION_J_PLUS_6)
    j_7 = get_jour(PREVISION_J_PLUS_7)

    _afficher_ligne_prevision("", j_1, j_2, j_3, j_4, j_5, j_6, j_7)
    print("|" + ("-" * (ECRAN_NOMBRE_COLONNES - 7)) + "|")

    for prevision in previsions:
        _afficher_ligne_prevision(prevision['description'], prevision['j1'], prevision['j2'], prevision['j3'],
                                  prevision['j4'], prevision['j5'], prevision['j6'], prevision['j7'])


def get_jour(period):
    """
    Obtient le jour de la semaine (Lundi, Mardi, etc.) à afficher en fonction du la période demandé et du jour actuel.
    ex : si l'on veur savoir quel est le jour de la semaine à J+2 en fonction du jour actuel (si on est mercredi, cela renvoi vendredi)
    :param period: PREVISION_AUJOURDHUI, PREVISION_J_PLUS_1, PREVISION_J_PLUS_2, etc... voir valeurs dans meteo_common.py
    :return: le jour calculé (chaine de caractères)
    """

    today = datetime.datetime.today()
    j_1 = today + datetime.timedelta(days=1)
    j_2 = today + datetime.timedelta(days=2)
    j_3 = today + datetime.timedelta(days=3)
    j_4 = today + datetime.timedelta(days=4)
    j_5 = today + datetime.timedelta(days=5)
    j_6 = today + datetime.timedelta(days=6)
    j_7 = today + datetime.timedelta(days=7)

    numero_jour = -1

    if period == PREVISION_AUJOURDHUI:
        numero_jour = today.isoweekday()
    if period == PREVISION_J_PLUS_1:
        numero_jour = j_1.isoweekday()
    if period == PREVISION_J_PLUS_2:
        numero_jour = j_2.isoweekday()
    if period == PREVISION_J_PLUS_3:
        numero_jour = j_3.isoweekday()
    if period == PREVISION_J_PLUS_4:
        numero_jour = j_4.isoweekday()
    if period == PREVISION_J_PLUS_5:
        numero_jour = j_5.isoweekday()
    if period == PREVISION_J_PLUS_6:
        numero_jour = j_6.isoweekday()
    if period == PREVISION_J_PLUS_7:
        numero_jour = j_7.isoweekday()

    if numero_jour == 1:
        return "Lundi"
    if numero_jour == 2:
        return "Mardi"
    if numero_jour == 3:
        return "Mercredi"
    if numero_jour == 4:
        return "Jeudi"
    if numero_jour == 5:
        return "Vendredi"
    if numero_jour == 6:
        return "Samedi"
    if numero_jour == 7:
        return "Dimanche"


def afficher_image_meteo(statut_image_meteo):
    """
    Affiche à l'écran le contenu du fichier texte correspondant au statut passé en paramètre
    :param statut_image_meteo: statut météo qui permet de choisir l'image appropriée, c'est à dire le bon fichier à ouvrir
    """
    chemin_reprtoire = os.path.dirname(__file__) + "/ressources/textes/"
    nom_image = ""

    if statut_image_meteo == STATUT_IMAGE_METEO_NEIGE:
        nom_image = "neige.txt"
    elif statut_image_meteo == STATUT_IMAGE_METEO_ORAGE:
        nom_image = "orage.txt"
    elif statut_image_meteo == STATUT_IMAGE_METEO_PLUIE:
        nom_image = "pluie.txt"
    elif statut_image_meteo == STATUT_IMAGE_METEO_SOLEIL:
        nom_image = "soleil.txt"
    elif statut_image_meteo == STATUT_IMAGE_METEO_NUAGEUX:
        nom_image = "nuageux.txt"
    elif statut_image_meteo == STATUT_IMAGE_METEO_ECLAIRCIES:
        nom_image = "eclaircies.txt"
    else:
        print("le statut pour l'image météo n'est pas reconnu, merci de vérivier votre code")

    chemin_image = chemin_reprtoire + nom_image
    fichier = open(chemin_image, 'r')
    contenu_fichier = fichier.read()
    print(contenu_fichier)
    fichier.close()


def afficher_ecran_accueil():
    """
    Affiche le premier écran qui permet à l'utilisateur de faire son choix entre recherche de ville et consultation directe
    """
    print("|" + ("-" * (ECRAN_NOMBRE_COLONNES - 3)) + "|")
    print("|" + (" " * (ECRAN_NOMBRE_COLONNES - 3)) + "|")
    print(_fermer_ligne("| Bienvenue dans ce programme météo, que souhaitez-vous faire ?"))
    print("|" + (" " * (ECRAN_NOMBRE_COLONNES - 3)) + "|")
    print(_fermer_ligne("|    1) Chercher une ville (tapez 1 et appuyez sur la touche entée)"))
    print(_fermer_ligne("|    2) Consulter la météo de sa ville (tapez 2 et appuyez sur la touche entée)"))
    print(_fermer_ligne("|    3) Selectionner parmis les villes les plus proche de chez moi (tapez 3 et appuyez sur "
                        "la touche entre)"))
    print(_fermer_ligne(f"|         {couleur.BOLD}Taper la touche Entrée pour quitter le programme{couleur.RESET}        "))
    print("|" + (" " * (ECRAN_NOMBRE_COLONNES - 3)) + "|")
    print("|" + ("-" * (ECRAN_NOMBRE_COLONNES - 3)) + "|")
    print()


def afficher_liste_ville(choix_ville_recherche):
    """
    Affiche la liste des villes issues du resulat de la recherche, avec une formatage permettant de présenter l'index
    pour chaque ville à l'utilisateur. Cet index sera utilisé ensuite pour que l'utilisateur indique son choix
    :param choix_ville_recherche:
    """
    print("Voicie la liste des villes trouvées :")
    for choix_ville in choix_ville_recherche.items():
        print('\t' + str(choix_ville[0]) + ") " + choix_ville[1])
