import numpy as np


class CovarianceFunctionEstimator:
    def __init__(self, values, N):
        self.N = N
        self.mean = np.array(values).mean()
        self.values = values
        self.x = np.random.chisquare(df=1, size=self.N)

    def estimate(self, h):
        return sum(map(lambda s: (self.values[s+h] - self.mean) * (self.values[s] - self.mean), range(self.N-h))) / (self.N-h)
