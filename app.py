def sum(num1, num2):
    sum = num1 + num2
    return sum


if __name__ == "__main__":
    num1 = float(input("enter you num1: "))
    num2 = float(input("enter you num2: "))
    result = sum(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")