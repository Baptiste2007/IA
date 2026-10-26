import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

print(" Tous les modules sont importés avec succès par mettez votre nom !")
# Mini test : graphique seaborn


df = pd.read_csv("Vitesse.csv")

sns.boxplot(x="Danger", y="Vitesse", data=df)
plt.title("Exemple graphique : vitesse selon danger")
plt.show()