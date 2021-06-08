from MarkovProcess import MarkovProcess
import numpy as np

class RandomWalk(MarkovProcess):
    def __init__(self, s=0, history=False):
        self.state = s
        self.history = None
        if history:
            self.history = [s]

    def get_state(self):
        return self.state

    def step(self):
        self.state += np.random.choice([-1, 1])
        if self.history:
            self.history.append(self.state)

def demo():
    r = RandomWalk(history=True)
    for i in range(100):
        r.step()
    r.plot_history()
