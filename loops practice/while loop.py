# ---------------- WHILE LOOP (1-10) ----------------

# 1. Print numbers 1 to 10
print("11. Numbers 1-10")
n = 1
while n <= 10:
    print(n, end=" ")
    n += 1
print("\n")

# 2. Odd numbers up to 20
print("12. Odd numbers")
n = 1
while n <= 20:
    print(n, end=" ")
    n += 2
print("\n")

# 3. Sum of 1 to 50
print("13. Sum of 1-50")
n, total = 1, 0
while n <= 50:
    total += n
    n += 1
print(total, "\n")

# 4. Countdown from 5
print("14. Countdown")
n = 5
while n > 0:
    print(n)
    n -= 1
print("Go!\n")

# 5. Table of 7
print("15. Table of 7")
n = 1
while n <= 10:
    print(f"7 x {n} = {7 * n}")
    n += 1
print()

# 6. Count digits of a number
print("16. Digits in 12345")
num, count = 12345, 0
while num > 0:
    num //= 10
    count += 1
print(count, "\n")

# 7. Reverse a number
print("17. Reverse of 1234")
num, rev = 1234, 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print(rev, "\n")

# 8. Sum of digits
print("18. Sum of digits of 4567")
num, s = 4567, 0
while num > 0:
    s += num % 10
    num //= 10
print(s, "\n")

# 9. break statement
print("19. Stop at 5 using break")
n = 1
while True:
    if n > 5:
        break
    print(n, end=" ")
    n += 1
print("\n")

# 10. continue statement (skip 3)
print("20. Skip 3 using continue")
n = 0
while n < 6:
    n += 1
    if n == 3:
        continue
    print(n, end=" ")
print()
