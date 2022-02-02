from art import logo

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operations = {
    "+": add, 
    "-": sub, 
    "*": mul, 
    "/": div
}

def Calculator():
    print(logo)

    num1 = float(input("What's the first number? "))

    runn = True
    while runn:
        num2 = float(input("What's the second number? "))
        print("Which of the following operation you want to perform?")

        for symbol in operations:
            print(symbol)
        opr = input("Pick an operation: ")

        calc = operations[opr]
        answer = calc(num1, num2)

        print(f"{num1} {opr} {num2} = {answer}")

        cont = input(f"Type 'y' to continue with {answer}, or type 'n' to exit.: ")
        
        if cont=='y':
            num1 = answer
        else:
            print("Goodbye")
            runn = False
            Calculator()

Calculator()