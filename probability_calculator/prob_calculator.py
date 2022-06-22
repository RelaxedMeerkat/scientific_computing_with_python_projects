import random
import copy


class Hat:
    def __init__(self, **ball_groups):
        self.contents = []
        for ball_type in ball_groups:
            for i in range(0, ball_groups[ball_type]):
                self.contents.append(str(ball_type))
        self.original = copy.deepcopy(self.contents)

    def draw(self, num_of_draws):
        balls_drawn = []
        if num_of_draws >= len(self.original):
            balls_drawn = self.original
        else:
            self.contents = copy.deepcopy(self.original)
            for i in range(0, num_of_draws):
                next_ball_index = random.randrange(len(self.contents))
                balls_drawn.append(self.contents[next_ball_index])
                del self.contents[next_ball_index]
        return balls_drawn
# class end

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    succesful_draws = 0
    for i in range(0, num_experiments):
        current_draw = list_to_dict(hat.draw(num_balls_drawn))
        draw_is_succesful = True
        for key in expected_balls:
            if key not in current_draw:
                draw_is_succesful = False
                break
            else:
                current_draw_int = current_draw[key]
                if current_draw_int < expected_balls[key]:
                    draw_is_succesful = False
                    break
        if draw_is_succesful:
            succesful_draws += 1

    probability = succesful_draws / num_experiments
    return probability


def list_to_dict(list):
  dict_to_return = {}
  for item in list:
    if item not in dict_to_return:
      dict_to_return[item] = 1
    else:
      dict_to_return[item] += 1
  return dict_to_return
