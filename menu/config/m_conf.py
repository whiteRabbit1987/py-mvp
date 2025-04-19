import random
from m_pack.menu_pkg import menu


def main():
    cart = []
    total = 0
    print("********MENU********")
    for key, value in menu.items():
        print(f"{key:10}: ${value:.2f}")
    print("********************")

    while True:
        food = input("What would you like?"
                     "\nq to quit | r for random: ")
        if food.lower() == 'q':
            break
        elif food.lower() == 'r':
            food = random.choice(list(menu.keys()))
            cart.append(food)
        elif menu.get(food) is not None:
            cart.append(food)
        else:
            print(f"{food} is not on the menu.")
    
    print(f"\n**********🍿You bought🍿**********\n")
    for food in cart:
        total += menu.get(food)
        print(food, end=" | ")
    print(f"\n\n**********Total: ${total:.2f}**********")