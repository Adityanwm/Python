operation = "divide"  
num1 = 2
num2 = 4

if operation == "add":
    result = num1 + num2
    print(result)

elif operation == "subtract":
    result = num1 - num2
    print(result)

elif operation == "multiply":
    result = num1 * num2
    print(result)

elif operation == "divide":
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("Division Error")

else:
    print("Invalid operation")