

def add(a,b):
    c=a+b
    print("sum=",c)

def sub(a,b):
    c=a-b
    print("difference=",c)

def mul(a,b):
    c=a*b
    print("product=",c)

def sub(a,b):
    c=a/b
    print("quotient=",c)

while(True):
    a =float(input('enter a value'))
    b =float(input('enter a value'))
        
    print("enter 1 to perform addition")
    print("enter 2 to perform subtraction")
    print("enter 3 to perform multiplication")
    print("enter 4 to perform division")

    c = int(input("Enter choice:"))

    match c:
        case 1:
            add(a,b)
        case 2:
            sub(a,b)
        case 3:
            mul(a,b)
        case 4:
            div(a,b)
        case 5:
            break

        case _:
            print("invalid choice")