from scipy.stats import multinomial

def calculate_odds(num_dice=0, difficulty=6):
	num_outcomes = 0
	odds_botch = .1
	odds_success = (11-difficulty)/10 
	odds_failure = 1 - odds_success - odds_botch
	distribution = multinomial(num_dice, [odds_botch, odds_failure, odds_success])
	outcome_odds = {}
	
	for num_botches in range(num_dice + 1):
		for num_failures in range((num_dice - num_botches) + 1):
			num_successes = num_dice - num_botches - num_failures
			odds = distribution.pmf([num_botches, num_failures, num_successes])
			outcome = num_successes - num_botches
			if outcome in outcome_odds:
				outcome_odds[outcome] = outcome_odds[outcome] + odds
			else:
				outcome_odds[outcome] = odds
	outcomes = sorted(list(outcome_odds.keys()))
	for outcome in outcomes:
		statement = "Odds of outcome {0} at Difficulty {1} = {2}".format(outcome, difficulty, outcome_odds[outcome])
		print(statement)

calculate_odds(5)
