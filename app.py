
import tkinter as tk
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


def verifier():

    vitesse = float(entree.get())

    resultat = Zpredict(vitesse)

    if resultat == 1:
        resultat_label.config(text="Dangereux !", fg="red")
    else:
        resultat_label.config(text="Safe !", fg="green")


fenetre = tk.Tk()
fenetre.title("Vérificateur de vitesse")

titre = tk.Label(fenetre, text="Entrez une vitesse :")
titre.pack()

entree = tk.Entry(fenetre)
entree.pack()

bouton = tk.Button(fenetre, text="Verifier", command=verifier)
bouton.pack()

resultat_label = tk.Label(fenetre, text="")
resultat_label.pack()

fenetre.mainloop()

