print("----------AutoCafe---------")
print('ESPRESSO-100\u20B9')
print('LATTE-200\u20B9')
print('CAPPUCINO-250\u20B9')
Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 200,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 250,
    },
}


resources = {
    "water": 300,
    "milk": 300,
    "coffee": 100,
}

profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    money_received = float(input("Please enter the money: "))
    return money_received

def is_transaction_success(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is \u20B9{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

is_on = True



while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: \u20B9{profit}")
    elif choice == "add resource":
        resources['water'] += int(input("Add water: "))
        resources['milk'] += int(input("Add milk: "))
        resources['coffee'] += int(input("Add coffee: "))
    elif choice == "remove profit":
        password = input("Enter the password to remove the profit: ")
        if password == "your_password":  # Replace "your_password" with the actual password
            print(f"Profit of \u20B9{profit} removed.")
            profit = 0
        else:
            print("Incorrect password. Unable to remove profit.")
    elif choice in Menu:
        drink = Menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice. Please try again.")
