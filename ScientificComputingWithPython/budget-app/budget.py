# TODO: build create_spend_chart func, remove test func calls
# TODO: make sure amounts in budget object output are max 7 characters
class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": abs(amount), "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == False:
            print("Failure")
            return False
        else:
            self.ledger.append({"amount": -abs(amount), "description": description})
            print("Success")
            return True

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance

    def transfer(self, amount, Category):
        if self.check_funds(amount) == False:
            return False
        else:
            self.ledger.append(
                {"amount": -abs(amount), "description": f"Transfer to {Category.name}"}
            )
            Category.ledger.append(
                {"amount": abs(amount), "description": f"Transfer from {self.name}"}
            )
            return True

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def view(self):
        print(self.ledger)
        print(self.get_balance())

    def __str__(self):
        returnstr = f"{self.name.center(30, '*')}\n"
        for i in self.ledger:
            amount = i["amount"]
            description = i["description"]
            returnstr += description[:23].ljust(23)
            returnstr += f"{amount:.2f}".rjust(7)
            returnstr += "\n"
        returnstr += f"Total: {self.get_balance():.2f}"
        return returnstr


def create_spend_chart(categories):
    withdrawals = []
    total_spent = 0
    for cat in categories:
        withdrawal_total = 0
        for trans in cat.ledger:
            if trans["amount"] < 0:
                withdrawal_total += trans["amount"]
        withdrawals.append(withdrawal_total)
        total_spent += withdrawal_total

    percentages = [((x / total_spent) * 100) for x in withdrawals]
    bar_chart = "Percentage spent by category\n"
    # generate y axis and bar part of chart
    for y_val in range(100, -10, -10):
        bar_chart += str(y_val).rjust(3, " ") + "|"
        for percent in percentages:
            if percent > y_val:
                bar_chart += " o "
            else:
                bar_chart += " " * 3
        bar_chart += " \n"
    # generate x axis
    bar_chart += " " * 4
    for category in categories:
        bar_chart += "---"
    bar_chart += "-\n"
    # print category names under x-axis and respective 'o' bars
    longest_category = max(len(category.name) for category in categories)
    for letter in range(longest_category):
        bar_chart += " " * 4
        for category in categories:
            if letter < len(category.name):
                bar_chart += " " + category.name[letter] + " "
            else:
                bar_chart += " " * 3

        bar_chart += " \n"
    bar_chart = bar_chart.rstrip() + " " * 2
    return bar_chart
