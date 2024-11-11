
from flask import Flask, render_template

app = Flask(__name__)

# read scores from the text file and return as a list of tuples
def get_scores_from_file(filename="scores.txt"):
    scores = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) == 2:
                player = parts[0].strip()  # Extract player name
                try:
                    score = int(parts[1].strip())  # Convert score to integer
                    scores.append((player, score))  # Add as a tuple to list of scores
                except ValueError:
                    print(f"Invalid score format for {player}: {parts[1].strip()}")
    return scores

# display the score table in HTML (at http://127.0.0.1:5000/score_table)
@app.route('/score_table')
def score_table():
    scores = get_scores_from_file()
    return render_template("score.html", scores=scores)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
