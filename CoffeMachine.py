from typing import ChainMap
import store as s

def getCoffeOptions():
    output = ""
    for key in s.menu:
        output += key + "/"
    return output

def reportMachine():
    print(f'Water: {s.resources["water"]} ml')    
    print(f'Milk: {s.resources["milk"]} ml')   
    print(f'Coffe: {s.resources["coffe"]} ml')   
    print(f'Profit: ${s.profit["total"]}')

def hasQunatity(drink):
    can_continue = True
    ingredients = s.menu[drink]["ingredients"]
    for key, value in ingredients.items():
        if s.resources[key] < value: 
            print(f"Sorry these is not enough {key}")
            can_continue = False
        return can_continue    

# print(getCoffeOptions())  

def proccessPayment(drink):
    payment = float(input("Insert amount: "))
    cost  = float(s.menu[drink]["cost"])
    if(cost>payment):
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = payment - cost
        if(change > 0):
            print(f"Here is ${change} in change") 
            s.profit["total"] += cost
            return True



def updateResources(drink):
    ingredients = s.menu[drink] ["ingredients"]
    for key, value in ingredients.items():
        s.resources[key] -= value              


offMachine = False
while not offMachine:
    command = input(f"What would u like? ({getCoffeOptions()}): ").lower()
    if command == "off":
        print("Thank you!")
        offMachine = True
    elif command == "report":
        reportMachine()  
    else:
        if hasQunatity(command):
            if(proccessPayment(command)):
                updateResources(command)
                print(f"Here is your {command.title()}. Enjoy!")

