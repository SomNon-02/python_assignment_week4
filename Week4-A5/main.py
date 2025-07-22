# Karanphol Nanthanawat
# Assignment 5.4

from Utilities.calculator import add, subtract, multiply, divide
from Utilities.string_operation import rev_str, cap_str, low_str, upp_str

print("Using calculator.py:")
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))

samp_str = "hello World"
print("\nUsing string_operations.py:")
print("Original:", samp_str)
print("Reversed:", rev_str(samp_str))
print("Capitalized:", cap_str(samp_str))
print("Lowercase:", low_str(samp_str))
print("Uppercase:", upp_str(samp_str))