from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import data

# menu
MENU = Menu()
ITEMS_NAMES = MENU.get_items()
ITEMS_NAMES_LIST = ITEMS_NAMES.split('/')

# coffee maker
COFFEE_MAKER = CoffeeMaker()

# menuItem
MENU_ITEMS = {}


# money_machine
MONEY_MACHINE = MoneyMachine()


def make_items():
    for i in data.MENU:
        new_item = MenuItem(i, data.MENU[i]['ingredients']['water'],
                            data.MENU[i]['ingredients']['milk'],
                            data.MENU[i]['ingredients']['coffee'],
                            data.MENU[i]['cost'])
        MENU_ITEMS[i] = new_item


def choosing_item():
    item = input(f'Choose one {ITEMS_NAMES}:').strip().lower()
    if item in ITEMS_NAMES_LIST:
        return item
    return False


make_items()

while True:
    print(COFFEE_MAKER.report())
    scan = choosing_item()
    if scan:
        print(scan)
        can_make_it = COFFEE_MAKER.is_resource_sufficient(MENU_ITEMS[scan])
        if not can_make_it:
            print('There ara no enough ingredients quantities')
            continue

        is_enough = MONEY_MACHINE.make_payment(MENU_ITEMS[scan].cost)

        if not is_enough:
            print('Money entered is not enough')
            continue
        print(f'Here is change ${round(MENU_ITEMS[scan].cost - MONEY_MACHINE.money_received, 2)}')
        COFFEE_MAKER.make_coffee(MENU_ITEMS[scan])
        print(f'Here is {scan}, enjoy')

    else:
        break
