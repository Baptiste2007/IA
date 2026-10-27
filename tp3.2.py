n = int(input("Entrez un entier n : "))

somme = 0

for i in range(1, n + 1):
    somme = somme + i

print("La somme de 1 à", n, "est :", somme)