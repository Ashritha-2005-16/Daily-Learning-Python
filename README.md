# Daily-Learning-Python

Daily Python practice: loops, basics and more.

I am learning Python step by step and pushing my practice code here every day.

## Progress

| Day |        Date |                                 Topic |
|-----|       ------|                                -------|
| 01  | 27 Nov 2026 | for loop and while loop (20 examples) |

## Day 01: Loops

### for loop
Used when you know how many times to repeat, or when going through a list or string.

```python
for i in range(1, 6):
    print(i)
```

- `range(start, stop, step)`: stop is not included
- Works on lists, strings and ranges

### while loop
Used to repeat until a condition becomes False.

```python
n = 1
while n <= 5:
    print(n)
    n += 1
```

- Always update the variable, or it becomes an infinite loop

### break and continue
- `break` stops the loop
- `continue` skips to the next round

## How to run

```
python day01_loops/loops_practice.py
```

## Goal
Learn one new Python topic every day and keep practising.
