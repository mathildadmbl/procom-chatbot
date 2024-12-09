nom = "Jean Dupont"
age = 35
profession = "Ingénieur"
score_epuisement = 45
score_detachement = 30

# Génération du fichier LaTeX
with open("variables.tex", "w", encoding="utf-8") as f:
    f.write(f"\\newcommand{{\\Nom}}{{{nom}}}\n")
    f.write(f"\\newcommand{{\\Age}}{{{age}}}\n")
    f.write(f"\\newcommand{{\\Profession}}{{{profession}}}\n")
    f.write(f"\\newcommand{{\\ScoreEpuisement}}{{{score_epuisement}}}\n")
    f.write(f"\\newcommand{{\\ScoreDetachement}}{{{score_detachement}}}\n")
print("Fichier variables.tex généré.")