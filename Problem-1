class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == "add":
            print(self.a + self.b)
        elif self.operation == "subtract":
            print(self.a - self.b)
        elif self.operation == "multiply":
            print(self.a * self.b)
        elif self.operation == "divide":
            if self.b != 0:
                print(self.a / self.b)
            else:
                print("Error: Division by zero")
        else:
            print("Invalid operation")

# Example input
a = 10.0
b = 5.0
operation = "divide"

calc = Calculator(a, b, operation)
calc.calculate()
