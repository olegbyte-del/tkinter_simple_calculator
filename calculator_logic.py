# Calculator logic

class operations: 
    
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
    