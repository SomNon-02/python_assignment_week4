# Karanphol Nanthanawat
# Assignment 3

add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b

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