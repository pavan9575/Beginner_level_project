import coffeeMaker_database
profit = 0
resources = {
        'milk' : 500,
        'coffe_beans':200,
        'water':800

    }
def process_coins():
    print("please insert coins : ")
    total = 0
    fiverupee_coins = int(input("please enter how many 5 rupee coins? : "))
    tenrupee_coins = int(input("enter how many 10 rupee coins? : "))
    hundredrupee_coins = int(input("enter how many hundred rupee coins?: "))
    total = fiverupee_coins*5 + tenrupee_coins*10 + hundredrupee_coins*100
    return total
def check_resources(order_ingredients):
    for item in resources:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry the {item} is not available")
            return False
    return True
def is_payment_succesful(money_received,coffe_cost):
    if money_received >= coffe_cost:
        global profit
        profit += coffe_cost
        change = money_received - coffe_cost
        print(f"Here is your rs{change}")
        return True
    else:
        print("money is not enough and its refunded")
        return False

def make_coffe(coffe_name,coffe_ingredient):
    for item in coffe_ingredient:
        resources[item] -=coffe_ingredient[item]
        print(f"Here is your {coffe_name} enjoy!!! ")
is_on = True
while is_on :
    choice = input("what would you like to have? (Espresso/Latte/Capuccino)")
    if choice == "off":
        is_on = False
        print("Coffe maker is turned off")
    elif choice == "report":
        print(f"Resources available are MILK = {resources['milk']}ml,COFFE BEANS = {resources['coffe_beans'] }gms and WATER = {resources['water']}ml")
        print(f"MONEY :{profit}")
    else:
        coffe_type = coffeeMaker_database.Menu[choice]
        print(coffe_type)
        if check_resources(coffe_type['ingredients']):
            payment = process_coins()
            if is_payment_succesful(payment,coffe_type['cost']):
                make_coffe(choice,coffe_type['ingredients'])
