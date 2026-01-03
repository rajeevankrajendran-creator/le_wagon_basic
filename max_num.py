a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

def max_num (a,b,c):
    if a > b and a > c:
        return f"{a} is the greatest number."
    elif b > a and b > c:
        return f"{b} is the greatest number."
    elif a == b or a == c or b == c:
        return f"There is a tie between the greatest numbers."
    else:
        return f"{c} is the greatest number."
    
print (max_num (a,b,c))