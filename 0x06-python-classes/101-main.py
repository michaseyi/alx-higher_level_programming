#!/usr/bin/python3
Square = __import__('101-square').Square

my_square = Square(5, (0, 0))
print("1==")
print(my_square)
print("2==")
my_square.my_print()
print("===")

print("--")

my_square = Square(5, (4, 1))
print("1==")
print(my_square)
print("2==")
my_square.my_print()
print("-==")
