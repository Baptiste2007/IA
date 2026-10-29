import pandas as pandasLib
import random

dataFrame1MonJeuDeDonneeDentrainement = pandasLib.read_csv("Vitesse.csv")

dataFrame1MonJeuDeDonneeDentrainement["Danger"] = dataFrame1MonJeuDeDonneeDentrainement["Danger"].map({False: 0, True: 1})

X = dataFrame1MonJeuDeDonneeDentrainement["Vitesse"].tolist()

Y = dataFrame1MonJeuDeDonneeDentrainement["Danger"].tolist()

print(X[:5], Y[:5])

w = random.randint(-10, 10)

b = random.randint(-10, 10)

def Zpredict(x):
    calcul = w*x+b
    if calcul >= 0:
        return 1
    else:
        return 0    
     

for x in X:
    print(f"x = {x}, prediction = { Zpredict(x)}")



for x, y in zip(X, Y):
    y_pred = Zpredict(x)
    erreur = y - y_pred

    print(f"x = {x}, y = {y}, y_pred = {y_pred}, erreur = {erreur}")

     