import prob_calculator

# set seed
prob_calculator.random.seed(95)

# create a hat with 4 blue balls, 2 red balls and 6 green balls
hat = prob_calculator.Hat(blue=4, red=2, green=6)

# run 3000 experiments and see the probability of drawing 4 balls (2 blue and 1 red at least)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)

# print the gotten probability
print("Probability:", probability)
