import matplotlib.pyplot as plt
import numpy as np

from randel.estimators.classic import classic_semivariogram_characteristic_function
from randel.estimators.covariance import CovarianceFunctionEstimator
from randel.estimators.expectation import calculate_expectation


def plot_process(values):
    fig, ax = plt.subplots()
    ax.plot(list(map(lambda x: x, range(len(values)))), values, '-o', markersize=3)
    plt.title("Случайный процесс")
    plt.show()


def plot_covariance_function(covariance_function, values):
    N = len(values)

    fig, ax = plt.subplots()
    x = np.arange(round(2*N/3 + 0.5))

    vectorized_covariance_function = np.vectorize(lambda x: covariance_function(x))
    ax.plot(x, vectorized_covariance_function(x), label="Ковариационная функция")

    estimator = CovarianceFunctionEstimator(values, N)
    vectorized_estimator = np.vectorize(estimator.estimate)
    ax.plot(x, vectorized_estimator(x), label="Оценка")

    plt.legend()
    plt.show()


def plot_semivariogram(semivariogram, estimator):
    fig, ax = plt.subplots()
    x = np.arange(round(estimator.N*2/3 + 0.5))

    vectorized_semivariogram = np.vectorize(semivariogram)
    ax.plot(x, vectorized_semivariogram(x), label="Семивариограмма")

    vectorized_estimator = np.vectorize(estimator.estimate)
    ax.plot(x, vectorized_estimator(x), label=estimator.label())

    plt.ylim(bottom=0)
    plt.legend()
    plt.show()


def plot_characteristic_function(covariance_function, h, simulator):
    fig, ax = plt.subplots()
    x = np.linspace(0, simulator.N, 100)

    covariance_matrix = np.zeros([simulator.N, simulator.N])
    for i in range(simulator.N):
        for j in range(simulator.N):
            covariance_matrix[i, j] = covariance_function(i - j)

    ax.plot(x, calculate_expectation(simulator, x, h, lambda x, y: np.exp(x * y * 1j)), label="ХФ процесса")
    ax.plot(x, classic_semivariogram_characteristic_function(simulator.N, covariance_matrix, h, x), label="ХФ chi-2")

    plt.legend()
    plt.show()