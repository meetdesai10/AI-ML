#  tuples are immutable
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tup)
print(len(tup))
print(tup[2])
print(tup[0:3])
print(tup[-6:-2])

sum = 0
for val in tup:
    sum += val

print(sum)
print(tup.index(6))
print(tup.count(2))
