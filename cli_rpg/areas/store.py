from items.items import loot_prices

def store(player):
    while True:
        print("\n****************************************************")
        print("🛖 Welcome to the town's store!"
              "\n1) Upgrade armour (+5 for 10 gold)"
              "\n2) Upgrade weapon (+5 for 20 gold)"
              "\n3) Sell loot."
              "\n4) Back to town.")
        print("****************************************************")
        
        choice = input("> ")
        if choice == '1':
            if player.gold >=10:
                player.gold -= 10
                player.hp += 5
                print("🛡️ You upgraded your armour.")
            else:
                print("❌ Not enough gold.")

        if choice == '2':
            if player.gold >= 20:
                player.gold -= 20
                player.damage += 5
                print(f"⚔️ You upgraded your weapon.")
            else:
                print("❌ Not enough gold.")

        elif choice == '3':
            if not player.loot:
                print("🪹 You have nothing to sell.")
            else:
                total = 0
                for item in player.loot:
                    price = loot_prices.get(item, 0)
                    total += price
                player.gold += total
                player.loot.clear()
                print(f"You earned {total} gold.")

        elif choice == '4':
            from areas.town import town_square
            town_square(player)
            break
        else:
            print("Invalid choice.")