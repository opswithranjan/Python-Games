from art import logo
def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
    print(logo)
    n1=float(input("Enter first number: "))
    n2=float(input("Enter second number: "))
    while True:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        calculation_function=operations[operation_symbol]
        first_answer=calculation_function(n1,n2)
        print(f"{n1}{operation_symbol}{n2}={first_answer}")
        cont=input(f"type 'y' to continue with previous result{first_answer} or type 'n' to start fresh calculation and type 'q' to exit: ")
        if cont=="y":
            n1=first_answer
            n2=float(input("Enter the next number: ")) 
        elif cont=='n':
            calculator()
        elif cont=='q':
            print("Thanks for using calculator.Have a good day! :-) ")
            break
calculator()

