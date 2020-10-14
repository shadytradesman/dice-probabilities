# Problem
What are the odds of M successes on N dice at difficulty D? 

This is fairly difficult to calculate, one is best served using a [trinomial distribution equation](https://online.stat.psu.edu/stat414/lesson/17/17.3) and [combinations with repetitions](https://www.cs.sfu.ca/~ggbaker/zju/math/perm-comb-more.html)

# Does this matter?

Do success / failure rates currently feel good in The Contract? Is combat “balanced?” Does the potential for wide interpretation of “partial” success make these odds unimportant?

Partial Successes and Botches give more power to the GM than complete or exceptional successes. We rely on the GM being good at managing the story, pacing, tension, and fairness of the game already, and this also falls into that category. 

A complete success takes power away from the GM, which is also desirable in certain situations. In Combat, partial successes have defined results (damage) and do not fall under GM discretion (though failures and botches still do). This helps combat feel “fair.” 

### When a GM sets a Difficulty, they are defining the odds between “GM discretion,”  “undeniable success,” and “undeniable failure.” 

Outside of combat, dice probabilities should be thought of in those terms.

A standard Difficulty of 6 means that experts are undeniably good at their tasks, but GMs are very likely to have to interpret a partial success for most.

# How to run this program:

clone repo and `cd` inside. Then:

`python3 -m venv env`

`source env/bin/activate`

`pip install -r requirements.txt`

`python diceprobs`

For now, you have to edit the source file to run different scenarios. May visualize later.

# How the math is done

The number of possible outcomes from rolling N 10-sided dice is easy to calculate. It is 10^N . This is a huge number, so a more useful question is: given N dice, rolled in the manner of The Contract, how many different results are possible accounting for the three outcomes (success, fail, botch)? The answer, it turns out, is C(N+2, 2) . See “combinations with repetitions” here for an explanation. 

So, for 5 dice, there are 21 different possible combinations of Success, Failure, Botch. That is a great improvement over the 10^5 possible outcomes we’d be worried about if we cared about all the numbers. 

We can assign an Outcome value to each of our cases by using our own knowledge of The Contract’s system: Outcome = successes - botches.  This Outcome value is used to interpret the results and derive more interesting results later.

Since we have split our results into a reasonable number of outcomes defined by number of Successes, Failures, and Botches, we can now exhaustively apply a trinomial distribution https://www.cs.sfu.ca/~ggbaker/zju/math/perm-comb-more.html 

This gives us the odds of each result. We can determine things like “What are the odds of getting at least X Outcome” by simple addition of the probabilities. This also allows us to easily derive datasets that cut across difficulties and dice numbers for set or threshold outcomes.

