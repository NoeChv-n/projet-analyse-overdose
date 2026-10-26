VALEURS_DETECTEES = ["Y", "y", "Y POPS", "Y (PTCH)"]


def convertir_en_booleens(tableau, colonnes, valeurs_detectees=VALEURS_DETECTEES):
    for colonne in colonnes:
        tableau[colonne] = tableau[colonne].isin(valeurs_detectees)
    return tableau