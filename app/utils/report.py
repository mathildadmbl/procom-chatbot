fichier = "result.txt"

def extraire_donnees(fichier):
    # Initialisation des variables
    nom = ""
    age = 0
    profession = ""
    score_epuisement = 0
    score_detachement = 0

    try:
        with open(fichier, "r") as f:
            for ligne in f:
                # Nettoyer la ligne pour enlever les espaces inutiles
                ligne = ligne.strip()
                
                # Vérification et extraction des valeurs
                if ligne.startswith("nom"):
                    nom = ligne.split("=", 1)[1].strip().strip('"')
                elif ligne.startswith("age"):
                    age = int(ligne.split("=", 1)[1].strip())
                elif ligne.startswith("profession"):
                    profession = ligne.split("=", 1)[1].strip().strip('"')
                elif ligne.startswith("score_epuisement"):
                    score_epuisement = int(ligne.split("=", 1)[1].strip())
                elif ligne.startswith("score_detachement"):
                    score_detachement = int(ligne.split("=", 1)[1].strip())

        return nom, age, profession, score_epuisement, score_detachement

    except FileNotFoundError:
        print(f"Le fichier '{fichier}' est introuvable.")
        return None
    except ValueError as e:
        print(f"Erreur lors de la conversion d'une valeur : {e}")
        return None


resultat = extraire_donnees(fichier)

if resultat:
    nom, age, profession, score_epuisement, score_detachement = resultat
    print(f"Nom : {nom}")
    print(f"Âge : {age}")
    print(f"Profession : {profession}")
    print(f"Score d'épuisement : {score_epuisement}")
    print(f"Score de détachement : {score_detachement}")


# Génération du fichier LaTeX
with open("variables.tex", "w", encoding="utf-8") as f:
    f.write(f"\\newcommand{{\\Nom}}{{{nom}}}\n")
    f.write(f"\\newcommand{{\\Age}}{{{age}}}\n")
    f.write(f"\\newcommand{{\\Profession}}{{{profession}}}\n")
    f.write(f"\\newcommand{{\\ScoreEpuisement}}{{{score_epuisement}}}\n")
    f.write(f"\\newcommand{{\\ScoreDetachement}}{{{score_detachement}}}\n")
print("Fichier variables.tex généré.")