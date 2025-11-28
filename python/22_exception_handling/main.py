# try
try:
    x = int(input("Enter a number: "))
    ans = 10/x

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

else:
    print(f"10 divided by {x} is {ans}")

finally:
    print("Execution completed.")
