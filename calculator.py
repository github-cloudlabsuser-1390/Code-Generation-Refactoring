import math

class ScientificCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, a, b):
        return math.pow(a, b)

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number.")
        return math.sqrt(a)

    def sin(self, a):
        return math.sin(math.radians(a))

    def cos(self, a):
        return math.cos(math.radians(a))

    def tan(self, a):
        return math.tan(math.radians(a))

    def log(self, a, base=10):
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive values.")
        return math.log(a, base)

    def ln(self, a):
        if a <= 0:
            raise ValueError("Natural logarithm undefined for non-positive values.")
        return math.log(a)


def main():
    calc = ScientificCalculator()
    print("Scientific Calculator")
    print("Available operations: add, subtract, multiply, divide, power, sqrt, sin, cos, tan, log, ln")
    while True:
        op = input("Enter operation (or 'exit' to quit): ").strip().lower()
        if op == 'exit':
            break
        try:
            if op in ['add', 'subtract', 'multiply', 'divide', 'power', 'log']:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if op == 'add':
                    print("Result:", calc.add(a, b))
                elif op == 'subtract':
                    print("Result:", calc.subtract(a, b))
                elif op == 'multiply':
                    print("Result:", calc.multiply(a, b))
                elif op == 'divide':
                    print("Result:", calc.divide(a, b))
                elif op == 'power':
                    print("Result:", calc.power(a, b))
                elif op == 'log':
                    print("Result:", calc.log(a, b))
            elif op in ['sqrt', 'sin', 'cos', 'tan', 'ln']:
                a = float(input("Enter number: "))
                if op == 'sqrt':
                    print("Result:", calc.sqrt(a))
                elif op == 'sin':
                    print("Result:", calc.sin(a))
                elif op == 'cos':
                    print("Result:", calc.cos(a))
                elif op == 'tan':
                    print("Result:", calc.tan(a))
                elif op == 'ln':
                    print("Result:", calc.ln(a))
            else:
                print("Unknown operation.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
