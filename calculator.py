print ("\n")
print ("Welcome to the Calculator Program!")
print ("----------------------------------")
num1 = float(input ("Enter the first number: "))
num2 = float(input ("Enter the second number: "))
ops = input ("Enter the operation (+, -, *, /): ")
print ("\n")

if ops == "+":
    result = num1 + num2
    print ("The result of " + str(num1) + " + " + str(num2) + " is: " + str(result))
elif ops == "-":
    result = num1 - num2
    print ("The result of " + str(num1) + " - " + str(num2) + " is: " + str(result))
elif ops == "*":
    result = num1 * num2
    print ("The result of " + str(num1) + " * " + str(num2) + " is: " + str(result))
elif ops == "/":   
    if num2 != 0:
        result = num1 / num2
        print ("The result of " + str(num1) + " / " + str(num2) + " is: " + str(result))
    else:
        print ("Error: Division by zero is not allowed.")
print ("\n")