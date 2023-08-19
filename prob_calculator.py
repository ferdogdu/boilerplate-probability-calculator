import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = list()
    for k, v in kwargs.items():
      for i in range(v):
        self.contents.append(k)

  def draw(self, number):
    balls = list()
    if number >= len(self.contents):
      balls = random.sample(self.contents, len(self.contents))
      self.contents.clear()
    else:
      for i in range(number):
        balls.append(random.choice(self.contents))
        self.contents.remove(balls[i])

    return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0

  for i in range(num_experiments):
    expected = list()
    for k, v in expected_balls.items():
      for i in range(v):
        expected.append(k)

    fresh_experiment = copy.deepcopy(hat)
    actual = fresh_experiment.draw(num_balls_drawn)

    for ball in actual:
      if ball in expected:
        expected.remove(ball)

    if (expected == []):
      M += 1

  return M / num_experiments
