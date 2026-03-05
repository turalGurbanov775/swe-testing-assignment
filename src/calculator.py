class Calculator:
    """Simple calculator for basic arithmetic operations."""

    def __init__(self) -> None:
        self.clear()

    def clear(self) -> float:
        """Reset current value to 0."""
        self.current = 0.0
        return self.current

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b