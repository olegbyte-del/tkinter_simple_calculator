# Calculator Gui

import calculator_logic as cl 
import tkinter as tk

calculator_actions = cl.CalFeatures()

class CalGui:
    
    def __init__(self, root):
        self.root = root 
        self.root.title("Calculator")
        self.root.geometry("500x500")
        self.feature = calculator_actions
        self.expression = ""
        
        self.display = tk.Entry(root, font=("Arial", 20), justify="right")
        self.display.pack(fill="both", padx=10, pady=10)