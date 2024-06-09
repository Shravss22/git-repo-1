def cel(a):
    c = 5/9(a-32)
    print(c)

def fah(a):
    f = (a * 9/5) + 32
    print(f)


while(True):
    a =float(input('enter a value'))
        
    print("enter 1 to convert fahrnheit to celsius")
    print("enter 2 to convert celsius to fahrenheit")
    

    c = int(input("Enter choice:"))

    match c:
        case 1:
            cel(a)
        case 2:
            fah(a)
        case 3:
            break

        case _:
            print("invalid choice")