
"""
Scoring chart:

Rock:     +1
Paper:    +2
Scissors: +3

Winning:  +6
Tie:      +3
Losing:   +0

"""

WIN = 6
TIE = 3
LOSE = 0

OPP_MAPPING = {
	"A": 1,
	"B": 2,
	"C": 3,
}

OWN_MAPPING = {
	"X": LOSE,
	"Y": TIE,
	"Z": WIN,
}


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
		opp_move = OPP_MAPPING[game[0]]
		own_win = OWN_MAPPING[game[1]]

		# Determine move
		if own_win == WIN:
			# Pick the winning move
			own_move = opp_move % 3 + 1
		elif own_win == TIE:
			# Pick the same move
			own_move = opp_move
		else:
			# Pick the losing move
			own_move = opp_move - 1 if opp_move - 1 > 0 else 3

		# Add score for win
		own_score += own_win
		opp_score += WIN - own_win

		# Add score for shape
		own_score += own_move
		opp_score += opp_move

	return own_score, opp_score


if __name__ == '__main__':
	games = read_games()

	own_score, opp_score = score_games(games)

	print(f"Own score:      {own_score}")
	print(f"Opponent score: {opp_score}")
