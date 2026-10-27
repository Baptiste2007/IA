n = int (input("entrer le nombre de note : "))
s = 0
for i in range(n):
 note = int (input("note :  "))
 s = s + note
 

moyenne = s / n
print("la moyenne est de : ", moyenne)