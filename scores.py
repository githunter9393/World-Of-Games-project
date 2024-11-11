def update_scores(player_name, difficulty):
    # Calculate points based on difficulty
    points = (3 * difficulty) + 5

    # Read the scores from scores.txt
    #  create a dictionary for a new scores table if necessary
    # the format of the scores will be 'user_name:score'
    try:
        with open('scores.txt', 'r') as file:
            lines = file.readlines()
            player_scores = {}
            for line in lines:
                player, score = line.strip().split(':')
                player_scores[player] = int(score)  # Convert score to an integer
    except FileNotFoundError:
        player_scores = {}

    # Update the score for new or existing users
    if player_name in player_scores:
        # adding points for an existing user
        player_scores[player_name] += points
    else:
        player_scores[player_name] = points

    # Write the name and score in scores.txt
    with open('scores.txt', 'w') as file:
        for player, score in player_scores.items():
            file.write(f"{player}:{score}\n")

