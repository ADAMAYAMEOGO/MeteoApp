import meteo
from meteo_common import *


def construire_affichage_prevision_temperature(ville, description, type_temperature):
    """
    Construit en mémoire un dictionnaire qui contient les données prévisionnelles de températures formatées en décimales
    -> cela permet un affichage basé sur le parcours du dictionnaire
    :param ville: ville sur laquelle porte la demande
    :param description:
    :param type_temperature:
    :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
    """
    previsions = {}

    previsions['description'] = description
    previsions['j1'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_1))
    previsions['j2'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_2))
    previsions['j3'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_3))
    previsions['j4'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_4))
    previsions['j5'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_5))
    previsions['j6'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_6))
    previsions['j7'] = "{:.1f}".format(meteo.get_temperature_prevision(ville, type_temperature, PREVISION_J_PLUS_7))

    return previsions


def construire_affichage_prevision_pression_athmospherique(ville):
    """
    Construit en mémoire un dictionnaire qui contient les données prévisionnelles athmosphériques formatées avec l'unité de mesure de pression (hPa)
    -> cela permet un affichage basé sur le parcours du dictionnaire
    :param ville: ville sur laquelle porte la demande
    :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
    """
    previsions = {}

    previsions['description'] = "Pression athm."
    previsions['j1'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_1)) + " hPa"
    previsions['j2'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_2)) + " hPa"
    previsions['j3'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_3)) + " hPa"
    previsions['j4'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_4)) + " hPa"
    previsions['j5'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_5)) + " hPa"
    previsions['j6'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_6)) + " hPa"
    previsions['j7'] = str(meteo.get_pression_athmospherique_prevision(ville, PREVISION_J_PLUS_7)) + " hPa"

    return previsions


def construire_affichage_prevision_avis_meteo_detaille(ville):
    """
    Construit en mémoire un dictionnaire qui contient l'avis météo détaillé prévisionnelle
    -> cela permet un affichage basé sur le parcours du dictionnaire
    :param ville: ville sur laquelle porte la demande
    :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
    """
    previsions = {}

    previsions['description'] = "Prévision"
    previsions['j1'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_1)
    previsions['j2'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_2)
    previsions['j3'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_3)
    previsions['j4'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_4)
    previsions['j5'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_5)
    previsions['j6'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_6)
    previsions['j7'] = meteo.get_avis_meteo_detaille_prevision(ville, PREVISION_J_PLUS_7)

    return previsions


def construire_affichage_prevision_humidite(ville):
    """
    Construit en mémoire un dictionnaire qui contient les prévisions d'humidité
    -> cela permet un affichage basé sur le parcours du dictionnaire
    :param ville: ville sur laquelle porte la demande
    :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
    """
    previsions = {}

    previsions['description'] = "Humidité"
    previsions['j1'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_1)) + "%"
    previsions['j2'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_2)) + "%"
    previsions['j3'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_3)) + "%"
    previsions['j4'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_4)) + "%"
    previsions['j5'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_5)) + "%"
    previsions['j6'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_6)) + "%"
    previsions['j7'] = str(meteo.get_humidite_prevision(ville, PREVISION_J_PLUS_7)) + "%"

    return previsions


def construire_affichage_prevision_vent_vitesse(ville):
    """
    Construit en mémoire un dictionnaire qui contient les prévisions de la vitesse du vent avec précision de l'unité
    -> cela permet un affichage basé sur le parcours du dictionnaire
    :param ville: ville sur laquelle porte la demande
    :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
    """
    previsions = {}

    previsions['description'] = "Vent (vitesse)"
    previsions['j1'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_1)) + " km/h"
    previsions['j2'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_2)) + " km/h"
    previsions['j3'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_3)) + " km/h"
    previsions['j4'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_4)) + " km/h"
    previsions['j5'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_5)) + " km/h"
    previsions['j6'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_6)) + " km/h"
    previsions['j7'] = "{:.1f}".format(meteo.get_vent_vitesse_prevision(ville, PREVISION_J_PLUS_7)) + " km/h"

    return previsions


def construire_affichage_prevision_vent_orientation(ville):
    """
    Construit en mémoire un dictionnaire qui contient les prévisions de l'orientation du vent avec précision de l'unité
    -> cela permet un affichage basé sur le parcours du dictionnaire
    :param ville: ville sur laquelle porte la demande
    :return: le dictionnaire qui contient les prévisions demandées pour la construction de l'affichage utilisateur
    """
    previsions = {}

    previsions['description'] = "Vent (direction)"
    previsions['j1'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_1)) + "°"
    previsions['j2'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_2)) + "°"
    previsions['j3'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_3)) + "°"
    previsions['j4'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_4)) + "°"
    previsions['j5'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_5)) + "°"
    previsions['j6'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_6)) + "°"
    previsions['j7'] = str(meteo.get_vent_orientation_prevision(ville, PREVISION_J_PLUS_7)) + "°"

    return previsions


