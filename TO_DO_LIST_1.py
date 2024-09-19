import tkinter as tk
from tkinter import messagebox

class TaskMaster:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_name, due_date=None):
        task_id = f"TM-{len(self.tasks) + 1}"
        self.tasks[task_id] = {"name": task_name, "due_date": due_date, "status": "pending"}
        return task_id

    def update_task(self, task_id, **kwargs):
        if task_id in self.tasks:
            for key, value in kwargs.items():
                self.tasks[task_id][key] = value
            return True
        else:
            return False

    def mark_done(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["status"] = "done"
            return True
        else:
            return False

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        else:
            return False

    def list_tasks(self):
        return self.tasks

class GUI:
    def __init__(self, master, task_master):
        self.master = master
        self.task_master = task_master
        self.tasks = self.task_master.list_tasks()

        self.task_name_label = tk.Label(master, text="Task Name:")
        self.task_name_label.grid(row=0, column=0)

        self.task_name_entry = tk.Entry(master)
        self.task_name_entry.grid(row=0, column=1)

        self.due_date_label = tk.Label(master, text="Due Date:")
        self.due_date_label.grid(row=1, column=0)

        self.due_date_entry = tk.Entry(master)
        self.due_date_entry.grid(row=1, column=1)

        self.add_task_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=2, column=0, columnspan=2)

        self.task_id_label = tk.Label(master, text="Task ID:")
        self.task_id_label.grid(row=3, column=0)

        self.task_id_entry = tk.Entry(master)
        self.task_id_entry.grid(row=3, column=1)

        self.update_task_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_task_button.grid(row=4, column=0, columnspan=2)

        self.mark_done_button = tk.Button(master, text="Mark Task as Done", command=self.mark_done)
        self.mark_done_button.grid(row=5, column=0, columnspan=2)

        self.delete_task_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=6, column=0, columnspan=2)

        self.list_tasks_button = tk.Button(master, text="List Tasks", command=self.list_tasks)
        self.list_tasks_button.grid(row=7, column=0, columnspan=2)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=8, column=0, columnspan=2)

        self.pending_tasks_screen = tk.Frame(master, bg="white")
        self.pending_tasks_screen.grid(row=0, column=2, rowspan=9, columnspan=3)

        self.pending_tasks_label = tk.Label(self.pending_tasks_screen, text="Pending Tasks:", bg="white")
        self.pending_tasks_label.pack()

        self.pending_tasks_text = tk.Text(self.pending_tasks_screen, bg="white", state=tk.DISABLED)
        self.pending_tasks_text.pack()

    def add_task(self):
        task_name = self.task_name_entry.get()
        due_date = self.due_date_entry.get()
        task_id = self.task_master.add_task(task_name, due_date)
        messagebox.showinfo("Task Added", f"Task '{task_name}' added with ID {task_id}!")
        self.update_pending_tasks()

    def update_task(self):
        task_id = self.task_id_entry.get()
        task_name = self.task_name_entry.get()
        due_date = self.due_date_entry.get()
        if self.task_master.update_task(task_id, name=task_name, due_date=due_date):
            messagebox.showinfo("Task Updated", f"Task {task_id} updated successfully!")
        else:
            messagebox.showerror("Task Not Found", f"Task {task_id} not found!")
        self.update_pending_tasks()

    def mark_done(self):
        task_id = self.task_id_entry.get()
        if self.task_master.mark_done(task_id):
            messagebox.showinfo("Task Marked as Done", f"Task {task_id} marked as done!")
        else:
            messagebox.showerror("Task Not Found", f"Task {task_id} not found!")
        self.update_pending_tasks()

    def delete_task(self):
        task_id = self.task_id_entry.get()
        if self.task_master.delete_task(task_id):
            messagebox.showinfo("Task Deleted", f"Task {task_id} deleted successfully!")
        else:
            messagebox.showerror("Task Not Found", f"Task {task_id} not found!")
        self.update_pending_tasks()

    def list_tasks(self):
        tasks = self.task_master.list_tasks()
        task_list = "To-Do List:\n"
        for task_id, task in tasks.items():
            task_list += f"  {task_id}: {task['name']} ({task['status']})\n"
        messagebox.showinfo("To-Do List", task_list)

    def update_pending_tasks(self):
        self.pending_tasks_text.config(state=tk.NORMAL)
        self.pending_tasks_text.delete(1.0, tk.END)
        tasks = self.task_master.list_tasks()
        for task_id, task in tasks.items():
            task_info = f"ID: {task_id}\nTask: {task['name']}\nDue Date: {task['due_date']}\nStatus: {task['status']}\n\n"
            self.pending_tasks_text.insert(tk.END, task_info)
        self.pending_tasks_text.config(state=tk.DISABLED)

root = tk.Tk()
task_master = TaskMaster()
gui = GUI(root, task_master)
root.mainloop()
