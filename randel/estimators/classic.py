import numpy as np

from randel.estimators.abstract import SemivariogramEstimator


class ClassicSemivariogramEstimator(SemivariogramEstimator):
    def __init__(self, N, values):
        self.N = N
        self.values = values

    def estimate(self, h):
        return sum(map(lambda s: (self.values[s+h] - self.values[s])**2, range(self.N-h))) / 2 / (self.N-h)

    def label(self):
        return "Классическая оценка"


def classic_semivariogram_characteristic_function(N, R, h, x_values):
    Q = np.zeros((N - h, N))
    for i in range(N - h):
        Q[i][i + h] = -1
        Q[i][i] = 1

    D = R[0][0]

    R_star = Q@R@Q.T / (2 * (N-h) * D)
    R_star_det = np.linalg.det(R_star)
    R_star_inv = np.linalg.inv(R_star)
    return list(map(lambda x: pow(R_star_det * np.linalg.det(R_star_inv - 2j * x * D * np.identity(R_star.shape[0])), -0.5), x_values))