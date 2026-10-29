def test(val):
    total = val*val
    print(total)

test(4)

noms = ["Baptiste", "Remond"]
ages = [19,20]
zipped = zip(noms,ages)
print(list(zipped))

for nom, age in zip(noms,ages):
    print(f"{nom} a {age} ans")

    z = zip(noms, ages)
    n, a = zip(*z)
    print(n)
    print(a)