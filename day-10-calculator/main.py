from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

do_calculation = True


def calculator():
    print(logo)
    global do_calculation
    num1 = float(input("What's the first number?: "))
    while do_calculation:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        question = input(
            "Do you want to continue? Type 'y' or 'n' for new calculation 'q' for quit: "
        )
        if question == "y":
            num1 = answer
        elif question != "n":
            calculator()
        else:
            do_calculation = False


calculator()
print("Goodbye")
