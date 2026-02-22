from player.player_selection import main as player_setup
from areas.town import town_square
from player.stats import print_stats

if __name__=="__main__":
    print("Welcome to Dragon Repeller (CLI RPG)!")
    player = player_setup()
    print_stats(player)
    town_square(player)