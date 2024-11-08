#TASK-3
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return 
    return a / b

while True:
    print("Select operation:\n1. Addition\t2. Subtraction\t3. Multiplication\t4. Division\t5. Exit")
    choice = input("Enter your choice: ")
    
    if choice in ('1', '2', '3', '4'):
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))

        if choice == '1':
            print(n1, "+", n2, "=", addition(n1, n2))
        elif choice == '2':
            print(n1, "-", n2, "=", subtraction(n1, n2))
        elif choice == '3':
            print(n1, "*", n2, "=", multiplication(n1, n2))
        elif choice == '4':
            print(n1, "/", n2, "=", division(n1, n2))
    
    elif choice == '5':
        break
    else:
        print("Invalid Input")