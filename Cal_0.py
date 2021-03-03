def add (a,b):
    print(a + b)

def sub (a,b):
    print(a-b)

def mul (a,b):
    print(a*b)

def div (a,b):
    print(a/b)

while(1):
    print("Choose Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    x = int(input("Select an Operation"))

    if ( x == 1):
        y = float(input("Enter First Operand"))
        z = float(input("Enter Second Operand"))
        add(y,z)
        continue
    if ( x == 2):
        y = float(input("Enter First Operand"))
        z = float(input("Enter Second Operand"))
        sub(y,z)
        continue
    if ( x == 3):
        y = float(input("Enter First Operand"))
        z = float(input("Enter Second Operand"))
        mul(y,z)
        continue
    if ( x == 4):
        y = float(input("Enter First Operand"))
        z = float(input("Enter Second Operand"))
        div(y,z)
        continue

    print("Invalid Input")
