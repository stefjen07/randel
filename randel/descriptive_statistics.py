import pandas as pd

class DescriptiveStatisticsCalculator:
    def calculate(self, values):
        series = pd.Series(values)
        self.mean = series.mean()
        self.median = series.median()
        self.asymmetry = series.skew()
        self.kurtosis = series.kurtosis()
        self.std = series.std()
        self.variance = self.std ** 2

    def print(self):
        print("Mean: " + str(self.mean))
        print("Median: " + str(self.median))
        print("Standard deviation: " + str(self.std))
        print("Variance: " + str(self.variance))
        print("Asymmetry coefficient: " + str(self.asymmetry))
        print("Kurtosis: " + str(self.kurtosis))