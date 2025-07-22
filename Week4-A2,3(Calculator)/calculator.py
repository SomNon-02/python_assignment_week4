# Karanphol Nanthanawat
# Assignment 2

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return ("Undefine")
    else:
        return a / b


x = int(input("Input value X : "))
y = int(input("Input value Y : "))
func = str(input("Input the function you want to use : "))

match func:
    case "Add":
        print(f"Addition : {add(x,y)}")   
    case "Subtract":
        print(f"subtraction : {subtract(x,y)}")
    case "Multiply":
        print(f"multiplication : {multiply(x,y)}")
    case "Divide":
        print(f"Divition : {divide(x,y)}")