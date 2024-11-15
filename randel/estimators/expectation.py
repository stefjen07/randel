import numpy as np

from randel.estimators.classic import ClassicSemivariogramEstimator


def calculate_expectation(simulator, x_values, h, func, iters=100):
    result = np.zeros(x_values.shape, dtype=np.float64)

    for _ in range(iters):
        estimator = ClassicSemivariogramEstimator(simulator.N-1, simulator.simulate_process())
        for i in range(len(x_values)):
            result[i] += func(x_values[i], estimator.estimate(h))

    return result / iters