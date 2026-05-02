# Calculator logic

class CalOperations: 
    
    def add(a, b):
        return a + b 
    
    def subtract(a, b): 
        return a - b 
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b): 
        if b == 0:
            raise ZeroDivisionError ("Cannot divide by ze")
        return a / b

    def expo(a, b):
        return a ** b

class CalFeatures:
    
    def __init__(self):
        self.math_expression = ""
        self.result = ""
        
    def save_memory(self.math_expression, self.result):
        with open("history.txt", "a") as file:
            file.write(f"{self.math_expression} = {self.result}")   