# TODO: Category.view not part of assignment
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
            returnstr += i["description"].ljust(23)
            returnstr += str(i["amount"]).rjust(7)
            returnstr += "\n"
        return returnstr


def create_spend_chart(categories):
    pass


# tests for Category class methods
gas = Category("gas")
food = Category("food")
food.deposit(10)
gas.deposit(40)
gas.transfer(food, 6.5)
food.view()
gas.view()
print(food)
