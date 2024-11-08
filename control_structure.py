#TASK-2
def classify_number():
  while True:
    num = input("Enter a number: ")
    num = num.lower() 
    if num=='exit':
        break
    else:
        num = int(num)
        if num > 0:
            print(" Number is Positive")
        elif num < 0:
            print("Number is Negative")
        elif num==0:
            print("Number is Zero")
        else:
            print("Input is invalid")

classify_number()

