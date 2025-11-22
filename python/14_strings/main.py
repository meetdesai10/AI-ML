word = "python"
word2 = "developer"

for ch in word:
    print(ch)
print(len(word))
print(word+word2)
print(word[0]+word2)

# slicing
print(word[0:3])
print(word[3:])  # empty second value if you want start to end index
print(word[:3])
print(word[-2:-4])


# formate strings
a = 5
b = 10
sum = a + b
print("Sum is {}".format(sum))
print("My name is {}".format("Meet Desai."))
# index base
print("My name is {0} and sum is {1}. my age is {2}".format(
    "Meet Desai.", sum, 23))

# f string
print(f"sum of {a} and {b} is {a+b}")


# strings are immutable in python
