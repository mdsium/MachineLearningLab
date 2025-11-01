# README.md

# Python Practice Tasks

A consolidated set of Python exercises with short, runnable code snippets. Use them one by one or copy into your editor.

---

## Basics

### 1) Print your name, department, and university

```python
name = "Md. Sium"
department = "Computer Science and Engineering (CSE)"
university = "Green University of Bangladesh"

print("Name:", name)
print("Department:", department)
print("University:", university)
```

### 2) Sum of two integers (input)

```python
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
print("Sum:", a + b)
```

### 3) Celsius to Fahrenheit

```python
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit:", f)
```

### 4) Area and perimeter of rectangle, circle, triangle

```python
import math

print("Choose shape: 1) Rectangle  2) Circle  3) Triangle")
choice = input("Enter 1/2/3: ").strip()

if choice == "1":
    length = float(input("Length: "))
    width = float(input("Width: "))
    area = length * width
    perimeter = 2 * (length + width)
    print("Rectangle area:", area)
    print("Rectangle perimeter:", perimeter)
elif choice == "2":
    r = float(input("Radius: "))
    area = math.pi * r * r
    circumference = 2 * math.pi * r
    print("Circle area:", area)
    print("Circle perimeter (circumference):", circumference)
elif choice == "3":
    a = float(input("Side a: "))
    b = float(input("Side b: "))
    c = float(input("Side c: "))
    perimeter = a + b + c
    s = perimeter / 2
    if a + b > c and a + c > b and b + c > a:
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print("Triangle area:", area)
        print("Triangle perimeter:", perimeter)
    else:
        print("Invalid triangle sides.")
else:
    print("Invalid choice.")
```

### 5) Simple and Compound Interest

```python
P = float(input("Principal (P): "))
R = float(input("Annual Rate % (R): "))
T = float(input("Time in years (T): "))

SI = (P * R * T) / 100
A_simple = P + SI
print("Simple Interest:", SI)
print("Amount with Simple Interest:", A_simple)

N = int(input("Compounds per year (N), e.g., 1, 2, 4, 12: "))
A_compound = P * (1 + (R / 100) / N) ** (N * T)
CI = A_compound - P
print("Compound Interest:", CI)
print("Amount with Compound Interest:", A_compound)
```

### 6) Unicode/ASCII value of a character

```python
ch = input("Enter a single character: ")
if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    code = ord(ch)
    print(f"Unicode code point of '{ch}' is {code} (hex: {hex(code)})")
```

### 7) Swap two numbers (with temp)

```python
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print("Before swap -> x:", x, "y:", y)
temp = x
x = y
y = temp
print("After swap  -> x:", x, "y:", y)
```

### 8) Swap two numbers (without temp)

```python
# Pythonic
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print("Before swap -> x:", x, "y:", y)
x, y = y, x
print("After swap  -> x:", x, "y:", y)
```

---

## Operators

### 1) Even or odd (modulo and bitwise)

```python
n = int(input("Enter an integer: "))
print("Even" if n % 2 == 0 else "Odd", "(modulo)")
print("Even" if (n & 1) == 0 else "Odd", "(bitwise)")
```

### 2) Maximum of three numbers

```python
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
mx = a
if b > mx: mx = b
if c > mx: mx = c
print("Max is:", mx)
```

### 3) Convert total days to years, weeks, days

```python
total_days = int(input("Total days: "))
years = total_days // 365
remaining = total_days % 365
weeks = remaining // 7
days = remaining % 7
print(f"{total_days} days = {years} years, {weeks} weeks, {days} days")
```

### 4) Minimum of two numbers (ternary)

```python
x = float(input("x: "))
y = float(input("y: "))
mn = x if x < y else y
print("Min is:", mn)
```

### 5) Pre vs post increment (Python illustration)

```python
def pre_inc(box):
    box[0] += 1
    return box[0]

def post_inc(box):
    old = box[0]
    box[0] += 1
    return old

i = [5]
print("Start i =", i[0])
print("pre_inc(i) ->", pre_inc(i))
print("After pre_inc, i =", i[0])
print("post_inc(i) ->", post_inc(i))
print("After post_inc, i =", i[0])
```

---

## Decision Making

### 1) Positive, negative, or zero

```python
n = float(input("Enter a number: "))
if n > 0: print("Positive")
elif n < 0: print("Negative")
else: print("Neutral (zero)")
```

### 2) Leap year check

```python
year = int(input("Enter a year: "))
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
```

### 3) Grade from marks

```python
marks = float(input("Enter marks (0-100): "))
if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

### 4) Character classification

```python
ch = input("Enter a single character: ")
if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    if ch.isdigit():
        print("Digit")
    elif ch.isalpha():
        print("Vowel" if ch.lower() in "aeiou" else "Consonant")
    else:
        print("Special symbol")
```

### 5) Simple calculator (match–case for Python 3.10+)

```python
a = float(input("First number: "))
op = input("Operator (+, -, *, /): ").strip()
b = float(input("Second number: "))
match op:
    case '+': print("Result:", a + b)
    case '-': print("Result:", a - b)
    case '*': print("Result:", a * b)
    case '/': print("Error: division by zero" if b == 0 else f"Result: {a / b}")
    case _: print("Invalid operator")
```

### 6) Greatest among three (if–else)

```python
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
if a >= b and a >= c: print("Greatest:", a)
elif b >= a and b >= c: print("Greatest:", b)
else: print("Greatest:", c)
```

### 7) Repeat input until 0 (loop in place of goto)

```python
while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        print("Stopped.")
        break
    print("You entered:", n)
```

---

## Loops

### 1) Print 1 to 100 (for, while, do-while style)

```python
for i in range(1, 101):
    print(i, end=" ")
print()

i = 1
while i <= 100:
    print(i, end=" ")
    i += 1
print()

i = 1
while True:
    print(i, end=" ")
    i += 1
    if i > 100:
        break
print()
```

### 2) Sum of first N natural numbers

```python
N = int(input("N: "))
total = 0
for i in range(1, N + 1):
    total += i
print("Sum =", total)
# Or: print("Sum =", N * (N + 1) // 2)
```

### 3) Factorial

```python
n = int(input("n: "))
fact = 1
for i in range(2, n + 1):
    fact *= i
print("Factorial =", fact)
```

### 4) Reverse a number

```python
n = int(input("n: "))
rev = 0
x = abs(n)
while x > 0:
    rev = rev * 10 + x % 10
    x //= 10
rev = -rev if n < 0 else rev
print("Reversed =", rev)
```

### 5) Count digits and sum of digits

```python
n = int(input("n: "))
x = abs(n)
count = 1 if x == 0 else 0
s = 0
while x > 0:
    s += x % 10
    x //= 10
    count += 1
print("Digits:", count if n != 0 else 1)
print("Sum of digits:", s if n != 0 else 0)
```

### 6) Multiplication table

```python
n = int(input("Number: "))
limit = int(input("Up to (e.g., 10): "))
for i in range(1, limit + 1):
    print(f"{n} x {i} = {n * i}")
```

### 7) All even numbers between two limits

```python
L = int(input("Lower: "))
R = int(input("Upper: "))
start = L if L % 2 == 0 else L + 1
for x in range(start, R + 1, 2):
    print(x, end=" ")
print()
```

### 8) Prime check

```python
n = int(input("n: "))
if n < 2:
    print("Not prime")
else:
    is_prime = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    print("Prime" if is_prime else "Not prime")
```

### 9) Perfect number

```python
n = int(input("n: "))
if n <= 1:
    print("Not perfect")
else:
    s = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
        i += 1
    print("Perfect" if s == n else "Not perfect")
```

### 10) Strong number

```python
n = int(input("n: "))

def fact(d):
    f = 1
    for i in range(2, d + 1):
        f *= i
    return f

x = n
s = 0
if x == 0:
    s = fact(0)
else:
    while x > 0:
        s += fact(x % 10)
        x //= 10
print("Strong number" if s == n else "Not a Strong number")
```

### 11) Spy number

```python
n = int(input("n: "))
x = abs(n)
s = 0
p = 1
if x == 0:
    s, p = 0, 0
else:
    while x > 0:
        d = x % 10
        s += d
        p *= d
        x //= 10
print("Spy number" if s == p else "Not a Spy number")
```

### 12) Armstrong number

```python
n = int(input("n: "))
x = abs(n)
digits = list(map(int, str(x)))
k = len(digits)
arm = sum(d ** k for d in digits)
print("Armstrong" if arm == x and n >= 0 else "Not Armstrong")
```

### 13) Palindrome number

```python
n = int(input("n: "))
x = abs(n)
rev = int(str(x)[::-1])
is_pal = (rev == x) and (n >= 0)
print("Palindrome" if is_pal else "Not Palindrome")
```