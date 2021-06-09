from MarkovProcess import MarkovProcess
import numpy as np

class BrownianMotion(MarkovProcess):
    def __init__(self, s=0, std=1, history=False):
        """
            @param s: initial state
            @param std: std dev for Gaussian step
        """
        self.state = s
        self.std = std
        self.history = None
        if history:
            self.history = [s]

    def get_state(self):
        return self.state

    def step(self):
        self.state += np.random.normal(scale=self.std)
        if self.history:
            self.history.append(self.state)

def demo():
    r = BrownianMotion(history=True)
    for i in range(100):
        r.step()
    r.plot_history()
