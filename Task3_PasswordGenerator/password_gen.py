import tkinter as tk
import random
import string
class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")

        tk.Label(root, text="🔐 Password Generator",
                 font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(root, text="Password Length").pack()
        self.length = tk.IntVar(value=12)
        tk.Spinbox(root, from_=4, to=30, textvariable=self.length).pack()

        tk.Button(root, text="Generate Password",
                  bg="#3498db", fg="white",
                  command=self.generate).pack(pady=10)

        self.output = tk.Entry(root, font=("Arial", 14))
        self.output.pack(fill="x", padx=20)

        tk.Button(root, text="Copy",
                  bg="#2ecc71", fg="white",
                  command=self.copy).pack(pady=10)

    def generate(self):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(chars) for _ in range(self.length.get()))
        self.output.delete(0, tk.END)
        self.output.insert(0, password)

    def copy(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.output.get())

if __name__ == "__main__":
    root = tk.Tk()
    PasswordGenerator(root)
    root.mainloop()
