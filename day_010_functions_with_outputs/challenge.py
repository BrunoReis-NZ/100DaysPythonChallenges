import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply (n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number? "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("What mathematical operator do you want? ")
        num2 = float(input("What is the second number? "))
        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'Yes' to continue calculating with {result} or type 'No' to start a new calculation: ")

        if choice == "Yes":
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()