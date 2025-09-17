first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = first + second
        print(f"The result is {result}.")
    
    case "-":
        result = first - second
        print(f"The result is {result}.")

    case "*":
        result = first * second
        print(f"The result is {result}.")

    case "/":
        if second == 0:
            print("Cannot divide by 0")
        else:
            result = first + second
            print(f"The result is {result}.")