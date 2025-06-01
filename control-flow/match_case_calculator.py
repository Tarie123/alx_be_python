num1 = int (input("Enter the first number: "))
num2 = int (input("Enter the second number: "))
ope = str(input("Choose the operation (+, -, *, /): "))

if ope == "+":
    sum = num1 + num2
elif ope == "-":
    sum = num1 - num2
elif ope == "*":
    sum = num1 * num2

elif ope == "/":
    sum = num1 / num2

print ("The result is", sum)
 