# you can create any variables here to store state within a run (but not between runs)
history = []

def play(reward, lockout, t, T, your_score, other_scores):
	"""
	Return True to accept the reward, False to skip.

	Called every round (including while locked out, so you can track history).
	If you are locked out, returning True has no effect.

	Parameters:
	    reward       - the reward offered this round (float)
	    lockout      - rounds you will be locked out if you accept (int)
	    t            - current round number, starting at 1 (int)
	    T            - total number of rounds (int)
	    your_score   - your cumulative score so far (float)
	    other_scores - list of other teams' current scores (list of floats)

	Returns:
	    bool - True to accept, False to skip
	"""
	history.append(reward)
	return True

