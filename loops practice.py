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

# ---------------- WHILE LOOP (11-20) ----------------

# 11. Print numbers 1 to 10
print("11. Numbers 1-10")
n = 1
while n <= 10:
    print(n, end=" ")
    n += 1
print("\n")

# 12. Odd numbers up to 20
print("12. Odd numbers")
n = 1
while n <= 20:
    print(n, end=" ")
    n += 2
print("\n")

# 13. Sum of 1 to 50
print("13. Sum of 1-50")
n, total = 1, 0
while n <= 50:
    total += n
    n += 1
print(total, "\n")

# 14. Countdown from 5
print("14. Countdown")
n = 5
while n > 0:
    print(n)
    n -= 1
print("Go!\n")

# 15. Table of 7
print("15. Table of 7")
n = 1
while n <= 10:
    print(f"7 x {n} = {7 * n}")
    n += 1
print()

# 16. Count digits of a number
print("16. Digits in 12345")
num, count = 12345, 0
while num > 0:
    num //= 10
    count += 1
print(count, "\n")

# 17. Reverse a number
print("17. Reverse of 1234")
num, rev = 1234, 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print(rev, "\n")

# 18. Sum of digits
print("18. Sum of digits of 4567")
num, s = 4567, 0
while num > 0:
    s += num % 10
    num //= 10
print(s, "\n")

# 19. break statement
print("19. Stop at 5 using break")
n = 1
while True:
    if n > 5:
        break
    print(n, end=" ")
    n += 1
print("\n")

# 20. continue statement (skip 3)
print("20. Skip 3 using continue")
n = 0
while n < 6:
    n += 1
    if n == 3:
        continue
    print(n, end=" ")
print()
