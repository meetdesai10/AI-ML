age = int(input("Enter your age:="))

# if else conditions
num = int(input("Enter the number:= "))

if (num % 2 == 0):
    print("Even")
else:
    print("Odd")

if (age > 13 and age < 18):
    print("tenager.")
elif (age >= 18):
    if (age >= 50):
        print("senior citizen.")
    else:
        print("adult.")
else:
    print("child.")


# match alternative of else if
color = input("Enter color :=")
match color:
    case "green":
        print("go")
    case "yellow":
        print("look")
    case "red":
        print("stop")
    case _:
        print("wrong color!")
