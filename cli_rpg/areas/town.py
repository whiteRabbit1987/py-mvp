
def town_square(player):
        if player.is_king:
               print("👑Long live the king!")
               player.gold += 10000
               
        print("\n****************************************************")
        print("You are in the town square. What would you like to do?")
        print("1) Go to store")
        print("2) Go to forest")
        print("3) Go to cave")
        print("4) Climb mountain")
        print("5) Visit Temple")
        print("6) Exit game")
        print("****************************************************")
        choice = input("> ")

        if choice == '1':
                from areas.store import store
                store(player)
        elif choice == '2':
                from areas.forest import forest
                forest(player)
        elif choice == '3':
                from areas.cave import cave
                cave(player)
        elif choice == '4':
                from areas.mountain import mountain_pass as mountain
                mountain(player)
        elif choice == '5':
               from areas.temple import sanctuary as heal
               heal(player)
        elif choice == '6':
                import sys
                sys.exit()
        else:
            print(f"{choice} is invalid.")
            town_square(player)