import pandas as pandasLib
import random

MonJeuDeDonnee = pandasLib.read_csv("Vitesse.csv")

MonJeuDeDonnee["Danger"] = MonJeuDeDonnee["Danger"].map({False: 0, True: 1})

X = MonJeuDeDonnee["Vitesse"].tolist()

Y = MonJeuDeDonnee["Danger"].tolist()

w = random.randint(-10, 10)

b = random.randint(-10, 10)

def Zpredict(x):
    calcul = w*x+b
    if calcul >= 0:
        return 1
    else:
        return 0


eta = 1.0
epochs = 570

for epoch in range(epochs):
    erreurs = 0
    for x, y in zip(X, Y):
        y_pred = Zpredict(x)
        erreur = y - y_pred
        if erreur != 0:
            w += eta * erreur * x
            b += eta * erreur
            erreurs += 1


print(f"Époque {epoch+1} : w = {w:.2f}, b = {b:.2f}, erreurs = {erreurs}")
if erreurs == 0:
    print("Apprentissage terminé.")


print("Prédictons après entraînement :")
for x in X:
    print(f"vitesse = {x} → danger prédit = {Zpredict(x)}")

    






