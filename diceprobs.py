from scipy.stats import multinomial
import json
from decimal import *


def calculate_odds(num_dice=0, difficulty=7, include_botches=True, include_doubles=True):
	odds_botch = Decimal('.1') if include_botches else Decimal('.0')
	odds_double = Decimal('.1') if include_doubles else Decimal('.0')
	odds_success = (Decimal('11')-difficulty)/Decimal('10') - odds_double
	odds_failure = Decimal('1') - odds_success - odds_botch - odds_double
	distribution = multinomial(Decimal(num_dice), [odds_botch, odds_failure, odds_success, odds_double])
	outcome_odds = {}
	
	for num_botches in range(num_dice + 1):
		for num_failures in range((num_dice - num_botches) + 1):
			for num_successes in range((num_dice - num_failures - num_botches) + 1):
				num_doubles = num_dice - num_botches - num_failures - num_successes
				odds = Decimal(distribution.pmf([Decimal(num_botches), Decimal(num_failures), Decimal(num_successes), Decimal(num_doubles)]))
				outcome = (num_successes - num_botches) + (2 * num_doubles)
				if num_botches + num_failures + num_successes + num_doubles > num_dice:
					print("{0} botches, {1} failures, {2} successes, {3} doubles".format(num_botches, num_failures, num_successes, num_doubles))
					raise ValueError('what')
				if odds > 0:
					if outcome in outcome_odds:
						outcome_odds[outcome] = outcome_odds[outcome] + odds
					else:
						outcome_odds[outcome] = odds
	# outcomes = sorted(list(outcome_odds.keys()))
	# for outcome in outcomes:
	# 	statement = "Odds of outcome {0} at Difficulty {1} with {2} dice = {3}".format(outcome, difficulty, num_dice, outcome_odds[outcome])
	# 	print(statement)
	for key in outcome_odds:
		outcome_odds[key] = float(outcome_odds[key])

	return outcome_odds

modes = ["standard", "botches", "doubles", "botchesAndDoubles"]

# outcomes = calculate_odds(num_dice=5, difficulty=6, include_botches=True, include_doubles=True)
outcomes_by_diff_by_dice_by_mode = {}
for mode in modes:
	botches = True
	doubles = True
	if mode == "standard":
		botches = False
		doubles = False
	elif mode == "botches":
		doubles = False
	elif mode == "doubles":
		botches = False
	outcomes_by_diff_by_dice = {}
	for dice in range(17):
		if dice > 0:
			outcomes_by_difficulty = {}
			for difficulty in range(10):
				if difficulty > 3:
					outcomes = calculate_odds(num_dice=dice, difficulty=difficulty, include_botches=botches, include_doubles=doubles)
					outcomes_by_difficulty[difficulty] = outcomes
			outcomes_by_diff_by_dice[dice] = outcomes_by_difficulty
	outcomes_by_diff_by_dice_by_mode[mode] = outcomes_by_diff_by_dice

print(json.dumps(outcomes_by_diff_by_dice_by_mode))
