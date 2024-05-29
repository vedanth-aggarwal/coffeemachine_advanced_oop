from replit import clear 
from time import sleep 
from prettytable import PrettyTable
x = PrettyTable()
logo = '''
             __  __                             _   _             
   ___ ___  / _|/ _| ___  ___    __ _ _ __   __| | | |_ ___  __ _ 
  / __/ _ \| |_| |_ / _ \/ _ \  / _` | '_ \ / _` | | __/ _ \/ _` |
 | (_| (_) |  _|  _|  __/  __/ | (_| | | | | (_| | | ||  __/ (_| |
  \___\___/|_| |_|  \___|\___|  \__,_|_| |_|\__,_|  \__\___|\__,_|


'''
coffee = '''
      )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'
'''
orders = []
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
def ressuf(drink):
  on = True
  for i in MENU[drink]['ingredients']:
    if MENU[drink]['ingredients'][i] >= resources[i]:
      print(f'---> Sorry there is not enough {i}')
      on = False
  return on 

def process_coins(drink):
  global total,profit 
  print("\nPlease insert coins : ")
  total = int(input("How many quarters?  ")) * 0.25
  total += int(input("How many dimes?  ")) * 0.1
  total += int(input("How many nickles?  ")) * 0.05
  total += int(input("How many pennies?  ")) * 0.01
  if total == MENU[drink]['cost']:
    print('No change')
    profit+=total
    return True
  elif total > MENU[drink]['cost']:
    print(f"\nChange : ${round(total-MENU[drink]['cost'],2)}")
    profit += round(total-MENU[drink]['cost'],2)
    return True
  else:
    print('\nInsufficient funds provided !')
    return False

def make_drink(drink,order):
  for i in MENU[drink]['ingredients']:
    resources[i] -= MENU[drink]['ingredients'][i]
  print(f'\nDrink Made - Here is your {drink}')
  order.append(drink)
  print(coffee)
  
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

gameon = True 
while gameon:
  x.clear()
  clear()
  print(logo)
  if not(orders):
    print("'1st order of the day'")
  elif len(orders) ==1:
    print(f"Previous order : {orders[0]}")
  else:
    print(f"Previous orders : ",end="")
    for i in orders:
      print(i,end=" | ")
  print()
  choice = input('Choose Drink:Latte $1.5 /Espresso $2.5 /Cappuccino $3.0 - ').lower()
  if choice =='off':
    print('MAINTAINENCE ONGOING')
    break
  elif choice == 'report':
    items = [' Water ',' Milk ',' Coffee ',' Cost ']
    values = []
    for i in resources:
      values.append(resources[i])
    values.append(profit)
    x.add_column('ITEM',items)
    x.add_column('VALUE',values)
    x.align == "c"
    print(x)
  else :
    if ressuf(choice):
      if process_coins(choice):
        make_drink(choice,orders)
  
  sleep(3)