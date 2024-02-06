################################
# Yonten Kinley Tenzin 
# SWE
# 02230313
################################
# REFERENCES
# https://www.w3schools.com/
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
################################
# SOLUTION
# Solution Score:49548
# input file 3
################################

def calculate_score(opponent_play, outcome):
    # Map the opponent's play to the player's choice
    player_choices = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    player_choice = player_choices[opponent_play]

    # Calculate the score based on the outcome
    if outcome == 'Y':
        return player_choice + 3
    elif outcome == 'Z':
        return player_choice + 6
    else:
        return player_choice

def main():
    input_file_name = '/Users/yontenkinleytenzin/Desktop/SWE_CAP1_02230313.py/input_3_cap1.txt'

    total_score = 0

    with open (input_file_name, 'r') as file:
        for line in file:
            opponent_play, outcome = line.strip().split()
            round_score = calculate_score(opponent_play, outcome)
            total_score += round_score

    print(f'Total Score: {total_score}')

if __name__ == "__main__":
    main()
    