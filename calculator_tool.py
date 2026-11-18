

class Calculator:
    def __init__(self):
        self.result = 0

    def multiply(self, num1, num2):
        self.result = num1 * num2
        return self.result

    def add(self, num1, num2):
        self.result = num1 + num2
        return self.result

    def subtract(self, num1, num2):
        self.result = num1 - num2
        return self.result

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        self.result = num1 / num2
        return self.result
