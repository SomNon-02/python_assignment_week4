# Karanphol Nanthanawat
# Assignment 4.2

import string_operation

samp_str = str(input("Input a string : "))
oper = str(input("Input an operation : "))

match oper:
    case "Reverse":
        print(string_operation.rev_str(samp_str))
    case "Capitalize":
        print(string_operation.cap_str(samp_str))
    case "Lowercase":
        print(string_operation.low_str(samp_str))
    case "Uppercase":
        print(string_operation.upp_str(samp_str))