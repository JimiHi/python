valid_input = False


while not valid_input:
    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        valid_input = True
    except ValueError as NumbersOnlyError:
        print(NumbersOnlyError)
        print("Numbers only")

that = input("Enter the method you want to do( add, minus, times or divide): ").lower()
try:
    if that == "add":
        equals = number1 + number2
        print(equals)
    elif that == "minus":
        equals = number1 - number2
        print(equals)
    elif that == "times":
        equals = number1 * number2
        print(equals)
    elif that == "divide":
        equals = number1 / number2
        print(equals)
    else:
        print("You entered an invaild option")
except ZeroDivisionError as e:
    print("You can't divide by zero")