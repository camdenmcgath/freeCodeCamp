# TODO: build create_spend_chart func, remove test func calls
# TODO: make sure amounts in budget object output are max 7 characters
class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": abs(amount), "description": description})

    def withdrawal(self, amount, description=""):
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

    def transfer(self, Category, amount):
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


# tests for Category class methods
clothing = Category("Clothing")
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdrawal(10.15, "grocieries")
food.withdrawal(15.89, "restaurant and more food")
food.transfer(clothing, 50)
print(food)


def create_spend_chart(categories):
    withdrawals = []
    total_spent = 0
    for cat in categories:
        withdrawal_total = 0
        for trans in cat.ledger():
            if trans["amount"] < 0:
                withdrawal_total += trans["amount"]
        withdrawals.append(withdrawal_total)
        total_spent += withdrawal_total

    percentages = [((x / total_spent) * 100) // 10 for x in withdrawals]
    # TODO build bar graph format
    # TODO build an array of size ll and fill with 'o's and spaces
    # use loop to append bar graph data to bar_chart
    # use range(0,len(categories)) to find column number
    # similar method for category name list, characters from end to start (spaces included)
    # also use loop to print out until longest name has been printed

    bar_chart = "Percentage spent by category\n"

    return bar_chart
