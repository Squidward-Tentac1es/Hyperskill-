water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550
machine_info = ''

def update_info():
    global machine_info
    machine_info = f"""The coffee machine has:
    {water} ml of water
    {milk} ml of milk
    {coffee_beans} g of coffee beans
    {disposable_cups} of disposable cups
    {money} of money
    """


def buy():
    global money
    global water
    global milk
    global coffee_beans
    global disposable_cups
    drinks = {"1": ("espresso", 250, 0, 16, 4),
              "2": ("latte", 350, 75, 20, 7),
              "3": ("cappuccino", 200, 100, 12, 6)}
    back = 'back'
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    choice = input()
    if choice == back:
        return None



    drink = drinks[choice]
    if water >= drink[1] and milk >= drink[2] and coffee_beans >= drink[3] and disposable_cups >= drink[4]:
        print('I have enough resources, making you a coffee!')
        water -= drink[1]
        milk -= drink[2]
        coffee_beans -= drink[3]
        money += drink[4]
        disposable_cups -= 1


    elif water <= drink[1]:
        print('Sorry, not enough water!')
    elif milk <= drink[2]:
        print('Sorry, not enough milk!')
    elif coffee_beans <= drink[3]:
        print('Sorry, not enough coffee_beans!')
    elif disposable_cups <= drink[4]:
        print('Sorry, not enough disposable_cups!')
    else:

        water -= drink[1]
        milk -= drink[2]
        coffee_beans -= drink[3]
        money += drink[4]
        disposable_cups -= 1


def fill():
    global water
    global milk
    global coffee_beans
    global disposable_cups
    print ('Write how many ml of water do you want to add:')
    water += int(input())
    print('Write how many ml of milk do you want to add:')
    milk += int(input())
    print('Write how many ml of coffee beans do you want to add:')
    coffee_beans += int(input())
    print('Write how many disposable cups of coffee beans do you want to add:')
    disposable_cups += int(input())


def take():
    global money
    print(f"I gave you ${money}")
    money = 0


def remaining():
    update_info()
    print(machine_info)


def exit():
    import sys
    sys.exit()

a = True
while a:

    actions = {"buy": buy, "fill":fill, "take":take, "remaining":remaining, "exit":exit}
    print('Write action (buy, fill, take, remaining, exit):')
    action = (input())
    actions[action]()
    print()



    if action == 'exit':
        a = False
