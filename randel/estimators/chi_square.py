import numpy as np

from randel.estimators.abstract import SemivariogramEstimator


class ChiSquareSemivariogramEstimator(SemivariogramEstimator):
    def __init__(self, N, covariance):
        self.N = N

        if type(covariance) is np.ndarray:
            self.covariance_matrix = covariance
        else:
            self.covariance_matrix = np.zeros([N, N])
            for i in range(N):
                for j in range(N):
                    self.covariance_matrix[i, j] = covariance(i - j)

        self.x = np.random.chisquare(df=1, size=self.N)

    def estimate(self, h):
        Q = np.zeros((self.N - h, self.N))
        for i in range(self.N - h):
            Q[i][i] = -1
            Q[i][i + h] = 1
        eigenvalues = np.linalg.eigvals(Q @ self.covariance_matrix @ Q.T / (self.N - h))

        return 0.5 * sum(map(lambda i: eigenvalues[i] * self.x[i], range(self.N-h)))

    def label(self):
        return "Оценка хи-квадрат"