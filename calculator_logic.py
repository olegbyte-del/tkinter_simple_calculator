# Calculator logic

class CalOperations: 
    """Basic arithmetic operation for the calculator such as addition,
    subtraction, multiplication, division, and exponent"""
    
    @staticmethod
    def add(a, b):
        """Peforms addition"""
        return a + b 
    
    @staticmethod
    def subtract(a, b): 
        """Peforms substraction"""
        return a - b 
    
    @staticmethod
    def multiply(a, b):
        """Peforms multiplication"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Peforms division and handles ZeroDivisionError"""
        if b == 0:
            raise ZeroDivisionError ("Cannot divide by ze")
        return a / b

    @staticmethod
    def expo(a, b):
        """Peforms power"""
        return a ** b

class CalFeatures:
    """Handles calculator features such as saving and loading history"""
    
    def __init__(self):
        self.math_expression = ""
        self.result = ""
        
    def save_memory(self, math_expression, result):
        """Save a calculation to history.txt and previous.txt file"""
        
        with open("previous.txt", "w") as file:
            file.write(f"{math_expression} = {result} \n") 
            
        with open("history.txt", "a") as file:
            file.write(f"{math_expression} = {result} \n")  
    
    def load_memory(self):
        """Loads all saved calculation history"""
        
        try:
            with open("history.txt", "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return []
        
    def load_previous(self):
        try:
            with open("previous.txt", "r") as file:
                return file.read()
        except FileNotFoundError:
            return ""
        
    