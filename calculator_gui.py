# Calculator Gui

import calculator_logic as cl 
import tkinter as tk

class CalGui:
    
    def __init__(self, root):
        
        self.first_num = ""
        self.operator = ""
        self.second_num = ""
        
        self.root = root 
        self.root.title("Calculator")
        self.root.geometry("200x280")
        
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
            tk.Button(frame, text=btn, width=5, height=2,
                    command=lambda x=btn: self.on_click(x)).grid(row=row, column=col)

            col += 1
            
            if col > 3:
                col = 0
                row +=1
