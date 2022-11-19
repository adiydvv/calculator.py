x = float(input("Enter a number: "))
op = input("Enter a operator(+, -, *, /, ^, sin, cos): ")

if op == "+":
    y = float(input("Enter second number: "))
    print(x + y)

elif op == "-":
    y = float(input("Enter second number: "))
    print(x - y)

elif op == "*":
    y = float(input("Enter second number: "))
    print(y * x)
elif op == "/":
    y = float(input("Enter second number: "))
    print(x / y)

elif op == "^":
    power = float(input("Enter power: "))
    print(x**power)

elif op == "sin":
    print(x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880 - x**11/39916800 + x**13/6227020800 - x**15/1307674368000)

elif op == "cos":
    print(1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320 - x**10/3628800 + x**12/479001600 - x**14/87178291200)
elif op == "tan":
    print((x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880 - x**11/39916800 + x**13/6227020800 - x**15/1307674368000)/(1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320 - x**10/3628800 + x**12/479001600 - x**14/87178291200))


else :
    print("invalid operator")




