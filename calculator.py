# Python calculator

flag = True

while flag:

    print("*************Python Calculator*************")

    operator = input("Enter and operator (+ - * /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operator == '+':
        result =  num1 + num2
        print(f"Result = {round(result, 2)}")
    elif operator == '-':
        result = num1 - num2
        print(f"Result = {round(result, 2)}")
    elif operator == '*':
        result = num1 * num2
        print(f"Result = {round(result, 2)}")
    elif operator == '/':
        result = num1 / num2
        print(f"Result = {round(result, 2)}")
    else:
        print(f"{operator} is not valid.")

    print("*************Python Calculator*************")

    end_program = input("Enter q to quit: ")
    if end_program == 'q':
        flag = False

