# 🍕 Online Pizza Shop

menu = {
    1: ("Pepperoni Pizza", 12.99),
    2: ("Margherita Pizza", 11.49),
    3: ("BBQ Chicken Pizza", 13.99),
    4: ("Hawaiian Pizza", 12.49),
    5: ("Veggie Pizza", 10.99),
    6: ("Meat Lovers Pizza", 14.99),
    7: ("Cheese Sticks", 5.99),
    8: ("Garlic Knots", 4.49),
    9: ("2-Liter Soda", 2.99)
}

foods = []
prices = []
total = 0

print("🍽️ Welcome to DoorDash Pizza Shop!")
print("Please select items from the menu below:")

while True:
    print("\n--- MENU ---")
    for number, (item, price) in menu.items():
        print(f"{number}. {item} - ${price:.2f}")

    choice = input("\nEnter item # to add to your cart (q to quit): ")

    if choice.lower() == 'q':
        break

    if choice.isdigit():
        choice = int(choice)
        if choice in menu:
            item_name, item_price = menu[choice]
            foods.append(item_name)
            prices.append(item_price)
            print(f"✅ {item_name} added to cart.")
        else:
            print("❌ Invalid item number. Please try again.")
    else:
         print("⚠️ Please enter a valid number or 'q' to quit.")

print("\n🧾 ******** YOUR ORDER ********")
for food in foods:
    print(f"- {food}")

total = sum(prices)
print(f"\n💰 Your total is: ${total:.2f}")
print("Thank you for ordering!")