from RPS_game import play, random_player
from RPS import player

# Play 1000 games and show the result
print("Playing against random_player:")
play(player, random_player, 1000, verbose=True)
