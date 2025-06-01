num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
match = str(input("Choose the operation (+, -, *, /): "))

if match == "+":
    sum = num1 + num2
elif match == "-":
    sum = num1 - num2
elif match == "*":
    sum = num1 * num2

elif match == "/":
    sum = num1 / num2

print ("The result is", sum)
 