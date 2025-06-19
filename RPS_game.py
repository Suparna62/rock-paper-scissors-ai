import random

def random_player(prev_play):
    return random.choice(["R", "P", "S"])

def play(player1, player2, num_games, verbose=False):
    player1_prev_play = ""
    player2_prev_play = ""

    player1_score = 0
    player2_score = 0

    for i in range(num_games):
        player1_move = player1(player2_prev_play)
        player2_move = player2(player1_prev_play)

        if verbose:
            print(f"Game {i+1}:")
            print(f"Player 1: {player1_move}  Player 2: {player2_move}")

        if player1_move == player2_move:
            if verbose:
                print("Result: Tie\n")
        elif (player1_move == "R" and player2_move == "S") or \
             (player1_move == "P" and player2_move == "R") or \
             (player1_move == "S" and player2_move == "P"):
            player1_score += 1
            if verbose:
                print("Result: Player 1 wins\n")
        else:
            player2_score += 1
            if verbose:
                print("Result: Player 2 wins\n")

        player1_prev_play = player1_move
        player2_prev_play = player2_move

    if verbose:
        print("Final Score:")
        print(f"Player 1: {player1_score}")
        print(f"Player 2: {player2_score}")

    return player1_score, player2_score
