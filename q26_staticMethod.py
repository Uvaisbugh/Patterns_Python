class Calculator:
    # Class attribute
    history = []

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Instance method (uses self)
    def add(self):
        result = self.a + self.b
        Calculator.history.append(f"{self.a} + {self.b} = {result}")
        return result

    # Class method (uses cls)
    @classmethod
    def show_history(cls):
        return cls.history

    # Static method (does not use self or cls)
    @staticmethod
    def multiply(x, y):
        return x * y

# Example usage
calc1 = Calculator(5, 3)
print("Addition:", calc1.add())  # Calls instance method

print("Multiplication (static method):", Calculator.multiply(4, 7))  # Calls static method

print("History (class method):", Calculator.show_history())  # Calls class method
