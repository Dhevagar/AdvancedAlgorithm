def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

# Example
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))
