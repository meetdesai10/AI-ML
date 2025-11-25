# append

# f = open("../sample.txt", "a")
# f.write("\nNew text added")

# create new file and add
# f = open("../sample2.txt", "x")
# f.write("random class")


# read and write together r+ is overriding the words you add
# f = open("../sample2.txt", "r+")
# f.write("123")

# read and write and append at the last
# f = open("../sample2.txt", "a+")
# f.write("\n123")

# everything will overwrite when writing
f = open("../sample2.txt", "w+")
f.write("\n123")
f.close()
