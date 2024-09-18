### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for ingredient, required_resources in ingredients.items():
            available_resources = self.machine_resources[ingredient]
            if available_resources < required_resources:
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        print("Sandwhich can be made")
        return True



    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input(how many quarters?: )"""
        dollar = int(input("How many dollar coins?: "))
        quarters = int(input("How many quarters?: ")) *.25
        dimes = int(input("How many dimes?: ")) *.10
        nickles = int(input("How many nickles?: ")) *.05
        balance = dollar + quarters + dimes + nickles
        print(f"Your balance is ${balance}.")
        return balance



    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = coins - cost
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return False


    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in order_ingredients.items():
            if self.machine_resources[ingredient] < amount:
                self.machine_resources[ingredient] -= amount
        print(f"{sandwich_size} sandwiches is ready. Bon appetit!")

        """Deduct the required ingredients from the resources.
           Hint: no output"""


### Make an instance of SandwichMachine class and write the rest of the codes ###

##machine.check_resources(recipes["small"]["ingredients"])
##machine.process_coins()
##machine.transaction_result(machine.process_coins(), recipes["small"]["cost"])
##machine.make_sandwich("small", recipes["small"]["ingredients"])

    def test(self):
        choice = input("What would you like? (small/medium/large/off/report): ")
        if choice == "small":
            machine.transaction_result(machine.process_coins(), recipes["small"]["cost"])
            machine.make_sandwich("small", recipes["small"]["ingredients"])
        if choice == "medium":
            machine.transaction_result(machine.process_coins(), recipes["medium"]["cost"])
            machine.make_sandwich("medium", recipes["medium"]["ingredients"])
        if choice == "large":
            machine.transaction_result(machine.process_coins(), recipes["large"]["cost"])
            machine.make_sandwich("large", recipes["large"]["ingredients"])
        if choice == "off":
            exit()
        if choice == "report":
            print(machine.machine_resources)

machine = SandwichMachine(resources)
machine.test()
machine.test()
machine.test()

