from abc import ABC, abstractmethod


class ProcessSimulator(ABC):
    @abstractmethod
    def simulate_process(self):
        pass