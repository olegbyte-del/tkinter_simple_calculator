# main program

from calculator_gui import CalGui
import tkinter as tk

def main():
    """Run main program"""
    root = tk.Tk()
    app = CalGui(root)
    root.mainloop()

if __name__ == "__main__":
    main()