import copy
import random



class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        print(kwargs)
        for key, value in kwargs.items():
            for efe in range(value):
                self.contents.append(key)
        print(self.contents)

    
    def draw(self, number_draws):
            drawn_balls = []

            if number_draws > len(self.contents):
                drawn_balls.extend(self.contents)
                self.contents.clear
                return drawn_balls
            else:
                for i in range(number_draws):
                    chosen_ball = random.choice(self.contents)
                    drawn_balls.append(chosen_ball)
                    self.contents.remove(chosen_ball)
            return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for efe in range(num_experiments): 
      expected_copy = copy.deepcopy(expected_balls)
      hat_copy = copy.deepcopy(hat)
      colors_gotten = hat_copy.draw(num_balls_drawn)

      for color in colors_gotten :
        if(color in expected_copy) :
          expected_copy[color] -= 1

      if(all(x <= 0 for x in expected_copy.values())):
        count += 1
          
    return count / num_experiments