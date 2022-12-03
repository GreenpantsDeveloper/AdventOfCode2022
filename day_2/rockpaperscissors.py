
"""
Scoring chart:

Rock:     +day_1
Paper:    +day_2
Scissors: +day_3

Winning:  +6
Tie:      +day_3
Losing:   +0

"""

OPP_MAPPING = {
	"A": 1,
	"B": 2,
	"C": 3,
}

OWN_MAPPING = {
	"X": 1,
	"Y": 2,
	"Z": 3
}

WIN = 6
TIE = 3
LOSE = 0


def read_games(filename='input.txt'):
	with open(filename, 'r') as fp:
		# Read the raw data
		games = fp.readlines()

	return [tuple(game.strip().split(' ')) for game in games]

def score_games(games):
	own_score = 0
	opp_score = 0

	for game in games:
		# Check moves
		own_move = OWN_MAPPING[game[1]]
		opp_move = OPP_MAPPING[game[0]]

		# Add score for shape
		own_score += own_move
		opp_score += opp_move

		# Add scores for win with move logic
		if own_move > opp_move and not (own_move == 3 and opp_move == 1):
			own_addition = WIN
		elif own_move == 1 and opp_move == 3:
			own_addition = WIN
		elif own_move == opp_move:
			own_addition = TIE
		else:
			own_addition = LOSE

		own_score += own_addition
		opp_score += WIN - own_addition

	return own_score, opp_score


if __name__ == '__main__':
	games = read_games()

	own_score, opp_score = score_games(games)

	print(f"Own score:      {own_score}")
	print(f"Opponent score: {opp_score}")
