import tkinter as tk
from tkinter import messagebox
import os

# -----------------------------
# MAIN APPLICATION CLASS
# -----------------------------
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("420x520")
        self.root.resizable(False, False)
        self.root.configure(bg="#ecf0f1")

        self.file_name = "tasks.txt"

        # -----------------------------
        # HEADER
        # -----------------------------
        header = tk.Label(
            root,
            text="📝 TO-DO LIST",
            font=("Segoe UI", 22, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=15
        )
        header.pack(fill="x")

        # -----------------------------
        # INPUT AREA
        # -----------------------------
        input_frame = tk.Frame(root, bg="#ecf0f1", pady=15)
        input_frame.pack()

        self.task_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 12),
            width=26,
            bd=0,
            relief="flat"
        )
        self.task_entry.pack(side="left", ipady=6, padx=(0, 10))

        add_btn = tk.Button(
            input_frame,
            text="Add",
            font=("Segoe UI", 11, "bold"),
            bg="#27ae60",
            fg="white",
            width=8,
            bd=0,
            cursor="hand2",
            command=self.add_task
        )
        add_btn.pack(side="left")

        # Hover effect
        add_btn.bind("<Enter>", lambda e: add_btn.config(bg="#2ecc71"))
        add_btn.bind("<Leave>", lambda e: add_btn.config(bg="#27ae60"))

        # -----------------------------
        # TASK LIST
        # -----------------------------
        self.listbox = tk.Listbox(
            root,
            font=("Segoe UI", 12),
            width=36,
            height=14,
            bd=0,
            selectbackground="#3498db",
            activestyle="none"
        )
        self.listbox.pack(pady=10)

        # -----------------------------
        # BUTTONS
        # -----------------------------
        btn_frame = tk.Frame(root, bg="#ecf0f1")
        btn_frame.pack(pady=10)

        self.create_button(btn_frame, "Mark Done", "#2980b9", self.mark_done, 0)
        self.create_button(btn_frame, "Delete", "#e74c3c", self.delete_task, 1)
        self.create_button(btn_frame, "Clear All", "#8e44ad", self.clear_all, 2)

        self.load_tasks()

    # -----------------------------
    # BUTTON CREATOR (CSS STYLE)
    # -----------------------------
    def create_button(self, frame, text, color, command, col):
        btn = tk.Button(
            frame,
            text=text,
            font=("Segoe UI", 11, "bold"),
            bg=color,
            fg="white",
            width=10,
            bd=0,
            cursor="hand2",
            command=command
        )
        btn.grid(row=0, column=col, padx=5)

        btn.bind("<Enter>", lambda e: btn.config(bg="#34495e"))
        btn.bind("<Leave>", lambda e: btn.config(bg=color))

    # -----------------------------
    # FUNCTIONS
    # -----------------------------
    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Warning", "Task cannot be empty!")
        else:
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            self.save_tasks()

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
            self.save_tasks()
        except:
            messagebox.showwarning("Warning", "Select a task first!")

    def mark_done(self):
        try:
            index = self.listbox.curselection()[0]
            task = self.listbox.get(index)
            if not task.startswith("✔"):
                self.listbox.delete(index)
                self.listbox.insert(index, "✔ " + task)
                self.save_tasks()
        except:
            messagebox.showwarning("Warning", "Select a task!")

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Clear all tasks?"):
            self.listbox.delete(0, tk.END)
            self.save_tasks()

    def save_tasks(self):
        with open(self.file_name, "w") as f:
            for task in self.listbox.get(0, tk.END):
                f.write(task + "\n")

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as f:
                for task in f:
                    self.listbox.insert(tk.END, task.strip())


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
