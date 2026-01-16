import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.expression = ""

        self.display = tk.Entry(root, font=("Arial", 18), justify="right")
        self.display.pack(fill="x", padx=10, pady=10)

        buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+"
        ]

        frame = tk.Frame(root)
        frame.pack()

        row = col = 0
        for btn in buttons:
            tk.Button(frame, text=btn, width=6, height=2,
                      command=lambda b=btn: self.click(b)).grid(row=row, column=col)
            col += 1
            if col == 4:
                col = 0
                row += 1

        tk.Button(root, text="Clear", bg="#e74c3c", fg="white",
                  command=self.clear).pack(fill="x", padx=10, pady=10)

    def click(self, value):
        if value == "=":
            try:
                self.display.delete(0, tk.END)
                self.display.insert(0, eval(self.expression))
                self.expression = ""
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        else:
            self.expression += value
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
