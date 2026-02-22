def battle(player, monster, place):
    while player.hp > 0 or monster['hp'] > 0:
        if player.damage >= monster['hp']:
            print(f"You've slain the {monster['name']} in one hit!")
            break
        else:
            print(f"The {monster['name']} attacks you! You loose {monster['damage']} healt points.")
            print(f"You strike back. The {monster['name']} looses {player.damage} health points.")
            player.hp -= monster['damage']
            monster['hp'] -= player.damage
            if player.hp <= 0:
                print(f"☠️ You have been killed by a {monster['name']}.")
                return
            elif monster['hp'] <= 0:
                print(f"You've slain the {monster['name']}!")
                break

    print(f"\nYou collect a {monster['loot']} and gain {monster['xp']} experience points.")
    player.xp += monster['xp']
    if monster['loot'] == 'Stone of Light' or monster['loot'] == 'Demon Staff' or monster['loot'] == 'Grimoire':
        player.items.append(monster['loot'])
    elif monster['loot'] == 'Dragon Heart':
        player.is_king = True
    else:
        player.loot.append(monster['loot'])
    print(f" XP: {player.xp} |  HP: {player.hp}")

    
    print("\nDo you want to: "
            f"\n1) Keep exploring the {place}"
            "\n2) Return to town")
    choice = input("> ")

    if choice == '2':
        from areas.town import town_square
        town_square(player)