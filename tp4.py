import pandas as pandasLib

dataFrame1MonJeuDeDonneeDentrainement = pandasLib.read_csv("Vitesse.csv")

dataFrame1MonJeuDeDonneeDentrainement["Danger"] = dataFrame1MonJeuDeDonneeDentrainement["Danger"].map({False: 0, True: 1})

X = dataFrame1MonJeuDeDonneeDentrainement["Vitesse"].tolist()

Y = dataFrame1MonJeuDeDonneeDentrainement["Danger"].tolist()

print(dataFrame1MonJeuDeDonneeDentrainement)