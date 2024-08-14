num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def plusNumber(num1, num2):
    return num1 + num2
def minusNumber(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divideNumber(num1, num2):
    if num2 != 0:
        return num1 // num2
    else:
        return "Error: Division by zero"

print("+ : ", plusNumber(num1, num2))
print("- : ", minusNumber(num1, num2))
print("* : ", multiply(num1, num2))
print("/ : ", divideNumber(num1, num2))
