sqr = []
for i in range(10):
    sqr.append(i*i)
print(sqr)

sq = [i*i for i in range(10)]
print(sq
      )
sq1 = [i*i for i in range(10) if i % 2 != 0]
print(sq1)

nums = [2, 6, -4, 5, -3, 4, -95, 7, 8, 6, -6, 3, -1]
nums = [0 if val < 0 else val for val in nums]
print(nums)

words = ["hello", "world", "python", "is", "awesome"]
words = [val.upper() for val in words]
print(words)
