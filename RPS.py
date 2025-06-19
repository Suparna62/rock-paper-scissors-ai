def player(prev_play, opponent_history=[]):
    import random

    # Add opponent's last move to history
    if prev_play:
        opponent_history.append(prev_play)

    # Default move
    guess = "R"

    if len(opponent_history) < 5:
        return guess

    # Use last 3 moves to detect patterns
    last3 = "".join(opponent_history[-3:])

    # Dictionary to store pattern counts
    patterns = {}

    for i in range(len(opponent_history) - 3):
        pattern = "".join(opponent_history[i:i+3])
        next_move = opponent_history[i+3]
        if pattern == last3:
            if next_move in patterns:
                patterns[next_move] += 1
            else:
                patterns[next_move] = 1

    if patterns:
        prediction = max(patterns, key=patterns.get)
    else:
        prediction = random.choice(["R", "P", "S"])

    # Choose the move that beats the prediction
    beats = {"R": "P", "P": "S", "S": "R"}
    return beats[prediction]
