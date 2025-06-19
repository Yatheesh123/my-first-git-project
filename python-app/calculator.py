# calculator.py

def add(a, b):
    return a + b

def main():
    print("Simple Calculator")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = add(a, b)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
