class Calculator:
    def __init__(self):
        self.clear()

    def clear(self):
        self.current = 0.0
        return self.current

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b