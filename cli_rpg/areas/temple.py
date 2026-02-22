import time

def sanctuary(player):
    while True:
        print("🏛️ You apporach an old man by the ancient temple."
              "\nWhat would you like to do? (each action takes time!)"
              "\n1) Meditate (+10 HP)"
              "\n2) Stay overnight (+25 HP)"
              "\n3) Stay a week (+125 HP)"
              "\n4) Return to town")
        
        choice = input("> ")

        if choice == '1':
            player.hp += 10
            print("🧘 You meditate in silence, feeling the energy of the temple flow into you.")
            print(f"✨ HP restored. Current HP: {player.hp}")
            time.sleep(5)
        elif choice == '2':
            player.hp += 25
            print("🛌 You stay overnight, resting in the peace of the sanctuary.")
            print(f"✨ HP restored. Current HP: {player.hp}")
            time.sleep(10)
        elif choice == '3':
            player.hp += 125
            print("⌛ You stay a full week, letting the temple's magic fully rejuvenate you.")
            print(f"✨ HP restored. Current HP: {player.hp}")
            time.sleep(20)
        elif choice == '4':
            from areas.town import town_square as town
            print("🚶 You thank the old man and head back to town.")
            town(player)
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")
            time.sleep(1)