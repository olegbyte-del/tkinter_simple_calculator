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
        
        self.operation = cl.CalFeatures()
        self.feature = cl.CalFeatures()
        self.expression = ""
        
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
    
    def calculate(self, value):
        try:
            expr = self.expression.replace("x", "*").replace("^", "**")
            
            self.display.insert(tk.END, "Press anything to start")
            
            num1 = float(self.first_num)
            num2 = float(self.second_num)
            
            if self.operation == "+": 
                result = cl.CalOperations.add(num1, num2)
            

            
            
            result = eval(expr)
            
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            
            self.expression = str(result)
        except ZeroDivisionError:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Cannot divide by 0")
            self.expression = ""
        
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""
            
    def on_click(self, value): 
        if value == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        
        elif value == "=": 
            self.calculate()
        
        else:
            self.expression += str(value)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)
        