from abc import ABC, abstractmethod


class SemivariogramEstimator(ABC):
    @abstractmethod
    def estimate(self, h):
        pass

    @abstractmethod
    def label(self):
        pass