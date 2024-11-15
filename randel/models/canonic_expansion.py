import numpy as np

from randel.models.abstract import ProcessSimulator


class CanonicExpansionSimulator(ProcessSimulator):
    def __init__(self, n, loc, covariance_function):
        self.n = n
        self.loc = loc
        self.covariance_function = covariance_function

    def simulate_process(self):
        variance = self.covariance_function(0)

        result = list()
        for t in range(self.n):
            value = 0
            for k in range(10):
                a = np.random.rayleigh(2 * variance)
                phi = np.random.uniform(-np.pi, np.pi)
                omega = 2 * np.pi / 150
                value += a * np.cos(k * omega * t + phi)
            result.append(self.loc + value)
        return result