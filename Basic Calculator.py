name = input("Hello, What's your name? ")
print("Nice to meet you, " + name + "!")

num1 = float(input("Hi, " + name + " Enter your first number: " ))
op = input("Please enter an operation (+, -, *, /): ")
num2 = float(input("now, enter the second number: "))

#control loop statements
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 !=0:
        result = num1 / num2
    else:
        result ="Oops, " + name + " error: division by zero"
else:
    result = "Invalid Operation. please " + name + " put the correct operation."

# to print result 
print(f"{num1:g} {op} {num2:g} = {result:g}")