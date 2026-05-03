# Calculator Gui

import calculator_logic as cl 
import tkinter as tk

class CalGui:
    
    def __init__(self, root):
        
        self.root = root 
        self.root.title("Calculator")
        self.root.geometry("280x300")
        
        self.first_num = ""
        self.operation = ""
        self.second_num = ""
        self.feature = cl.CalFeatures()
        
        self.display = tk.Entry(root, font=("Arial", 25), justify="left")
        self.display.pack(fill="both", padx=10, pady=10)
        
        self.icon = tk.PhotoImage(file="calculator_logo.png")
        self.root.iconphoto(True, self.icon)
        
        frame = tk.Frame(root)
        frame.pack()
        
        buttons = ["1", "2", "3", "C",
                "4", "5", "6", "+",
                "7", "8", "9", "-",
                "0", "x", "/", "^",
                "="]
        
        row = 0
        col = 0
        for btn in buttons:
            if btn == "=":
                tk.Button(
                    frame,
                    text=btn,
                    width=32,
                    height=2,
                    command=lambda x=btn: self.on_click(x)
                ).grid(row=row, column=0, columnspan=4)
            else:
                tk.Button(frame, 
                        text=btn, 
                        width=7, 
                        height=2,
                        command=lambda x=btn: self.on_click(x)
                ).grid(row=row, column=col)
                col += 1
                
                if col > 3:
                    col = 0
                    row +=1
    
    def calculate(self):
        try:
            
            num1 = float(self.first_num)
            num2 = float(self.second_num)
            
            if self.operation == "+": 
                result = cl.CalOperations.add(num1, num2)
            
            elif self.operation == "-":
                result = cl.CalOperations.subtract(num1, num2)
            
            elif self.operation == "x":
                result = cl.CalOperations.multiply(num1, num2)
            
            elif self.operation == "/": 
                result = cl.CalOperations.divide(num1, num2)
            
            elif self.operation == "^": 
                result = cl.CalOperations.expo(num1, num2)
            
            else: 
                result = "Error"
            
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            
            self.first_num = str(result)
            self.second_num = ""
            self.operation = ""
            

        except ZeroDivisionError:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Cannot divide by 0")
            self.first_num = ""
            self.second_num = ""
            self.operation = ""
        
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.first_num = ""
            self.second_num = ""
            self.operation = "" 
            
    def on_click(self, value): 
        if value == "C":
            self.first_num = ""
            self.second_num = ""
            self.operation = ""
            self.display.delete(0, tk.END)
            
        elif value == "=": 
            self.calculate()
            
        else:
            operators = ["+", "-", "x", "/", "^"]
            
            if value in operators:
                if self.first_num == "": 
                    return 
                if self.operation != "":
                    return
                
                self.operation = value
                self.display.insert(tk.END, value)
                
            elif self.first_num and not self.operation:
                    self.operation = value
                    
            else:
                self.display.insert(tk.END, value)
                if self.operation == "":
                    self.first_num += value
                else:
                    self.second_num += value
            