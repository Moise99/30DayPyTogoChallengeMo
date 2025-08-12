# 1. Create a class called PersonAccount

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}   # {description: amount}
        self.expenses = {}  # {description: amount}

    def add_income(self, description, amount):
        self.incomes[description] = self.incomes.get(description, 0) + amount

    def add_expense(self, description, amount):
        self.expenses[description] = self.expenses.get(description, 0) + amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return (
            f"Account Holder: {self.firstname} {self.lastname}\n"
            f"Total Income: {self.total_income()}\n"
            f"Total Expense: {self.total_expense()}\n"
            f"Balance: {self.account_balance()}\n"
            f"Incomes: {self.incomes}\n"
            f"Expenses: {self.expenses}"
        )
    

    
account = PersonAccount('Koffi', 'Kouma') 
account.add_income('Salary', 3000)
account.add_income('Freelance', 1200)
account.add_expense('Rent', 1000)
account.add_expense('Groceries', 300)
account.add_expense('Utilities', 150)

print(account.account_info())
