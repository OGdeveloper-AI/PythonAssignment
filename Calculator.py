#Calculator


#Addition

def add(x, y):
    return x + y

#Subtraction
def subtract(x, y):
    return x - y

#Multiplication
def multiply(x, y):
    return x * y

#Divison
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    User_Input = input("Enter your required operation(1/2/3/4): ")


    if User_Input in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    
        if User_Input == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif User_Input == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif User_Input == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
    
        elif User_Input == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break        
    else:
        print("Invalid input")
        
