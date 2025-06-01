num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
operation = str(input("Choose the operation (+, -, *, /): "))

if operation == "+":
    sum = num1 + num2
elif operation == "-":
    sum = num1 - num2
elif operation == "*":
    sum = num1 * num2

elif operation == "/":
    sum = num1 / num2

print ("The result is", sum)
 