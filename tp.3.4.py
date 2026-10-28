a = int(input("Type a value of the number a "))
b = int(input("Type a value of the number b "))
c = int(input("Type a value of the number c "))

max = 0
if(a > b):
    max = a
else:
    max = b
if(max < c):
    max = c
else:
    max = max
print("Le maximum des trois nombre est : max(a,b,c) = ", max)