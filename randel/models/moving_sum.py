import numpy as np
from scipy.optimize import fsolve


def equations(p, covariance_values):
    n = len(p)

    equations = -covariance_values
    for i in range(n):
        for j in range(n-i):
            equations[i] += p[j] * p[i+j]
    return equations


def solve(values, start_xs):
    result = list()
    norm = 100
    for start_x in start_xs:
        new_result = list(fsolve(equations, start_x, args=values))
        print(new_result)
        new_norm = max(list(map(abs, equations(new_result, values))))
        print(new_norm)

        if new_norm < norm:
            result = new_result
            norm = new_norm
    return result


class MovingSumSimulator:
    def __init__(self, N, T, loc, covariance_function):
        self.N = N
        self.delta_t = T / N
        self.loc = loc
        self.covariance_function = covariance_function
        self.coefficients = self.find_coefficients()

    def find_coefficients(self):
        values = np.array(list(map(lambda x: self.covariance_function(x * self.delta_t), range(self.N))))
        return solve(values, list(map(lambda x: np.random.random(size=self.N), range(3))) + values)

    def simulate_process(self):
        x = np.random.normal(loc=self.loc, scale=1, size=self.N * 2)

        result = list()
        for t in range(self.N):
            result.append(sum(map(lambda k: x[t-k] * self.coefficients[k], range(self.N))))
        return result