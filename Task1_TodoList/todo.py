import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.tasks = []

        tk.Label(root, text="📝 To-Do List", font=("Arial", 18, "bold")).pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(fill="x", padx=20)

        tk.Button(root, text="Add Task", bg="#2ecc71", fg="white",
                  command=self.add_task).pack(pady=10)

        self.listbox = tk.Listbox(root, font=("Arial", 12))
        self.listbox.pack(fill="both", expand=True, padx=20)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Delete", bg="#e74c3c", fg="white",
                  command=self.delete_task).pack(side="left", padx=5)

        tk.Button(btn_frame, text="Clear All", bg="#7f8c8d", fg="white",
                  command=self.clear_tasks).pack(side="left", padx=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Enter a task")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
            self.tasks.pop(index)
        except:
            messagebox.showwarning("Warning", "Select a task")

    def clear_tasks(self):
        self.listbox.delete(0, tk.END)
        self.tasks.clear()

if __name__ == "__main__":
    root = tk.Tk()
    TodoApp(root)
    root.mainloop()
