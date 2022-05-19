"""Probability Calculator Project for the Scientific Computing With Python
certfication of freeCodeCamp. This project calculates the probability
of drawing certain colored balls from a hat"""

import copy
import random

# Consider using the modules imported above.


class Hat:
    """Class that constructs instances of hats containing
    colored balls to perform probability calculations on"""

    # Constructor
    def __init__(self, **colors):
        """Constructor that creates Hat instances.
        colors: color of ball and number,
        then converted to contents list var"""
        # self.contents = []
        # for key, value in colors.items():
        #    self.contents += value * [key]
        self.contents = [
            (str(key)) for key in colors.keys() for value in range(colors.get(key))
        ]

    # Other methods
    def draw(self, num):
        """Randommly removes ball from hat contents and
        returns those balls as list of strings"""
        if num > len(self.contents):
            return self.contents
        else:
            return [
                self.contents.pop(self.contents.index(random.choice(self.contents)))
                for x in range(num)
            ]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Args: hat- balls to be copied in function
    expected_balls- group of balls attempting to be drawn from hat
    num_balls_drawn- num of balls drawn out of hat each experiment
    num_experiments- number of experiments to perform
    Returns probability that expected_balls are found in a draw from hat"""
    matches = 0
    for x in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        balls_drawn = experiment_hat.draw(num_balls_drawn)
        # Convert expected balls to list from dict
        expected = [
            (str(key))
            for key in expected_balls.keys()
            for value in range(expected_balls.get(key))
        ]
        match_true = True
        # check if draw contains all expected balls
        for ball in expected:
            if ball not in balls_drawn or balls_drawn.count(ball) < expected.count(
                ball
            ):
                match_true = False
                break
        if match_true:
            matches += 1
    return matches / num_experiments
