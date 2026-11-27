"""
Python Basics: for loop and while loop (20 examples)
Date learnt: 27 Nov 2026
"""

# ---------------- FOR LOOP (1-10) ----------------

# 1. Print numbers 1 to 10
print("1. Numbers 1-10")
for i in range(1, 11):
    print(i, end=" ")
print("\n")

# 2. Print even numbers up to 20
print("2. Even numbers")
for i in range(2, 21, 2):
    print(i, end=" ")
print("\n")

# 3. Sum of 1 to 100
print("3. Sum of 1-100")
total = 0
for i in range(1, 101):
    total += i
print(total, "\n")

# 4. Multiplication table of 5
print("4. Table of 5")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
print()

# 5. Print each letter of a word
print("5. Letters in 'Python'")
for ch in "Python":
    print(ch)
print()

# 6. Loop through a list
print("6. Fruits list")
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
print()

# 7. Reverse count 10 to 1
print("7. Countdown")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")

# 8. Factorial of 5
print("8. Factorial of 5")
fact = 1
for i in range(1, 6):
    fact *= i
print(fact, "\n")

# 9. Star pattern
print("9. Star pattern")
for i in range(1, 6):
    print("*" * i)
print()

# 10. Square of numbers 1 to 5
print("10. Squares")
for i in range(1, 6):
    print(f"{i} squared = {i ** 2}")
print()

