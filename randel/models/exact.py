import numpy as np

from randel.models.abstract import ProcessSimulator


class FirstSimulator(ProcessSimulator):
    def __init__(self, N, D, alpha):
        self.N = N
        self.T = N
        self.D = D
        self.alpha = alpha

    def simulate_process(self):
        delta_t = self.T / self.N
        gamma = self.alpha * delta_t
        a = np.sqrt(self.D * (1 - np.exp(-2 * gamma)))
        b = np.exp(-gamma)

        result = [a * np.random.standard_normal()]
        for _ in range(self.N-1):
            result.append(a * np.random.standard_normal() + b * result[-1])
        return result


class SecondSimulator(ProcessSimulator):
    def __init__(self, N, D, alpha):
        self.N = N
        self.T = N
        self.D = D
        self.alpha = alpha

    def simulate_process(self):
        x = np.random.normal(loc=0, scale=1, size=self.N * 2)
        p = round(2 / self.alpha)

        delta_t = self.T / self.N
        gamma = self.alpha * delta_t
        c = np.array(2*p+1)
        for k in range(-p, p+1):
            c[k] = np.sqrt(self.D / np.pi / self.alpha) * (1 if k == 0 else np.sin(self.alpha * k) / k)

        result = list()
        for t in range(self.N):
            result.append(sum(map(lambda k: c[k] * x[t-k], range(-p, p+1))))
        return result


class ThirdSimulator(ProcessSimulator):
    def __init__(self, N, D, alpha):
        self.N = N
        self.D = D
        self.alpha = alpha

    def simulate_process(self):
        new_n = self.N + self.alpha - 1
        x = np.random.normal(loc=0, scale=1, size=new_n * 2)

        result = list()
        for t in range(new_n):
            result.append(np.sqrt(self.D / self.alpha) * sum(map(lambda k: x[t - k], range(self.alpha))))
        return result[self.alpha:]