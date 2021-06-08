from abc import ABC, abstractmethod
from matplotlib import pyplot as plt

class MarkovProcess(ABC):
    @abstractmethod
    def step(self):
        """Compute the next state and set it as the current state"""
        pass

    @abstractmethod
    def get_state(self):
        """Return the current state"""
        pass

    def plot_history(self):
        if self.history:
            plt.plot(self.history)
            plt.show()
