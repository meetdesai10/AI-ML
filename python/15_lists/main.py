marks = [99, 95, 94, 96, 93, 97]
marks[1] = 100
print(marks)
print(len(marks))
print(marks[0:5])
print(marks[-5:-3])

# methods od f list
marks.append(500)
marks.insert(2, 210)
marks.sort()
# marks.sort(reverse=True)
marks.reverse()
print(marks)


# string are immutable but list are mutable
