import tkinter as tk

class Numina:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def adda(self):
        return self.num1 + self.num2

    def subba(self):
        return self.num1 - self.num2

    def multa(self):
        return self.num1 * self.num2

    def diva(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero!"
    
    def powa(self):
        return self.num1 ** self.num2

class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.num1_label = tk.Label(master, text="Number 1:")
        self.num1_label.grid(row=0, column=0)

        self.num1_entry = tk.Entry(master)
        self.num1_entry.grid(row=0, column=1)

        self.num2_label = tk.Label(master, text="Number 2:")
        self.num2_label.grid(row=1, column=0)

        self.num2_entry = tk.Entry(master)
        self.num2_entry.grid(row=1, column=1)

        self.operation_label = tk.Label(master, text="Operation:")
        self.operation_label.grid(row=2, column=0)

        self.operation_var = tk.StringVar()
        self.operation_var.set("+")
        self.operation_menu = tk.OptionMenu(master, self.operation_var, "+", "-", "*", "/", "^")
        self.operation_menu.grid(row=2, column=1)

        self.calculate_button = tk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=3, column=0, columnspan=2)

        self.result_label = tk.Label(master, text="Result:")
        self.result_label.grid(row=4, column=0)

        self.result_text = tk.Text(master, height=1, width=20)
        self.result_text.grid(row=4, column=1)

    def calculate(self):
        num1 = float(self.num1_entry.get())
        num2 = float(self.num2_entry.get())
        operation = self.operation_var.get()

        numina = Numina(num1, num2)

        if operation == "+":
            result = numina.adda()
        elif operation == "-":
            result = numina.subba()
        elif operation == "*":
            result = numina.multa()
        elif operation == "/":
            result = numina.diva()
        elif operation == "^":
            result = numina.powa()
        else:
            result = "Error: Invalid operation!"

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, str(result))

root = tk.Tk()
calculator_gui = CalculatorGUI(root)
root.mainloop()
