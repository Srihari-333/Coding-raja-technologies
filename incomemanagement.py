import tkinter as tk
from tkinter import messagebox

class BudgetTrackerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Tracker")

        self.balance = 0
        self.transactions = []

        # Income Section
        income_frame = tk.Frame(self.root, padx=10, pady=10)
        income_frame.pack()

        tk.Label(income_frame, text="Add Income", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)

        tk.Label(income_frame, text="Amount:").grid(row=1, column=0, sticky=tk.E)
        self.income_amount_entry = tk.Entry(income_frame)
        self.income_amount_entry.grid(row=1, column=1)

        tk.Label(income_frame, text="Description:").grid(row=2, column=0, sticky=tk.E)
        self.income_desc_entry = tk.Entry(income_frame)
        self.income_desc_entry.grid(row=2, column=1)

        income_btn = tk.Button(income_frame, text="Add Income", command=self.add_income)
        income_btn.grid(row=3, column=0, columnspan=2, pady=10)

        # Expense Section
        expense_frame = tk.Frame(self.root, padx=10, pady=10)
        expense_frame.pack()

        tk.Label(expense_frame, text="Add Expense", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)

        tk.Label(expense_frame, text="Amount:").grid(row=1, column=0, sticky=tk.E)
        self.expense_amount_entry = tk.Entry(expense_frame)
        self.expense_amount_entry.grid(row=1, column=1)

        tk.Label(expense_frame, text="Category:").grid(row=2, column=0, sticky=tk.E)
        self.expense_category_entry = tk.Entry(expense_frame)
        self.expense_category_entry.grid(row=2, column=1)

        tk.Label(expense_frame, text="Description:").grid(row=3, column=0, sticky=tk.E)
        self.expense_desc_entry = tk.Entry(expense_frame)
        self.expense_desc_entry.grid(row=3, column=1)

        expense_btn = tk.Button(expense_frame, text="Add Expense", command=self.add_expense)
        expense_btn.grid(row=4, column=0, columnspan=2, pady=10)

        # Balance Section
        balance_frame = tk.Frame(self.root, padx=10, pady=10)
        balance_frame.pack()

        tk.Label(balance_frame, text="Current Balance", font=("Arial", 14)).pack()

        self.balance_label = tk.Label(balance_frame, text=f"${self.balance}", font=("Arial", 18, "bold"))
        self.balance_label.pack()

        # Transactions Section
        transactions_frame = tk.Frame(self.root, padx=10, pady=10)
        transactions_frame.pack()

        tk.Label(transactions_frame, text="Transactions by Category", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)

        self.category_entry = tk.Entry(transactions_frame)
        self.category_entry.grid(row=1, column=0)

        view_transactions_btn = tk.Button(transactions_frame, text="View Transactions", command=self.view_transactions)
        view_transactions_btn.grid(row=1, column=1, padx=10)

        self.transactions_text = tk.Text(transactions_frame, width=50, height=10)
        self.transactions_text.grid(row=2, column=0, columnspan=2, pady=10)

    def add_income(self):
        try:
            amount = float(self.income_amount_entry.get())
            description = self.income_desc_entry.get()
            self.balance += amount
            self.transactions.append({"type": "Income", "amount": amount, "description": description})
            self.update_balance()
            self.clear_income_entries()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def add_expense(self):
        try:
            amount = float(self.expense_amount_entry.get())
            category = self.expense_category_entry.get()
            description = self.expense_desc_entry.get()
            self.balance -= amount
            self.transactions.append({"type": "Expense", "amount": amount, "category": category, "description": description})
            self.update_balance()
            self.clear_expense_entries()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def update_balance(self):
        self.balance_label.config(text=f"${self.balance}")

    def clear_income_entries(self):
        self.income_amount_entry.delete(0, tk.END)
        self.income_desc_entry.delete(0, tk.END)

    def clear_expense_entries(self):
        self.expense_amount_entry.delete(0, tk.END)
        self.expense_category_entry.delete(0, tk.END)
        self.expense_desc_entry.delete(0, tk.END)

    def view_transactions(self):
        self.transactions_text.delete(1.0, tk.END)
        category = self.category_entry.get().strip()
        for transaction in self.transactions:
            if category:
                if transaction.get("type") == "Expense" and transaction.get("category") == category:
                    self.transactions_text.insert(tk.END, f"{transaction}\n")
            else:
                self.transactions_text.insert(tk.END, f"{transaction}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetTrackerGUI(root)
    root.mainloop()