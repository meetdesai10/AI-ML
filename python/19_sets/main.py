
# sets is unique if you store duplicates then it will not stores
# unorder
set = {
    1, 2, 3, 4, 5, 6, 6
}


# set2 = set()  # empty sets


# methods

set.add(10)
set.remove(4)
set.pop()
# set.clear()
print(set)

set2 = {1, 2, 3, 4, 5}
set3 = {4, 5, 8, 9, 10}
print(set2.union(set3))
# return duplicate values array
print(set2.intersection(set3))
