x = 1
y = 1
z = 2
n = 3

listA = [[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a+b+c != n]


print(listA)