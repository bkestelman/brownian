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

def brownian_bridge(res=100):
    b = BrownianMotion(history=True)
    b.step()
    first = b.state
    reset = False
    while not reset:
        b.step()
        if (first > 0 and b.state < 0) or (first < 0 and b.state > 0):
            b.state = 0
            b.history[-1] = 0
            reset = True
    return b

def demo():
    r = BrownianMotion(history=True)
    for i in range(100):
        r.step()
    r.plot_history()
    bridge = brownian_bridge()
    bridge.plot_history()
