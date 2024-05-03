#Calculator(using functions)
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y 
def division(x,y):
    if y == 0:
        return "Cannot divide by Zero!"
    else:
        return x/y 
def caclculator():
    print("Select Operation.")
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    
    choice = input("Enter a choice: ")
    
    num1=int(input("Enter the first number: "))
    num2=int(input("Enter the second number: "))
    
    if choice == '1':
        print("RESULT:",add(num1,num2))
    elif choice == '2':
        print("RESULT:",subtract(num1,num2))
    elif choice == '3':
        print("RESULT:",multiply(num1,num2))
    elif choice =='4':
        print("RESULT:",divide(num1,num2))
    else:
        print("INVALID INPUT.")
caclculator()  