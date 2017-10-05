import pandas as pd
import numpy

from bioinput import Bioinput

class Biomeasure():
    """

    """

    def __init__(self, threshold=0.9):
        self.__hr_rawdata = pd.DataFrame(numpy.empty((10, 3))*numpy.nan, columns=['HeartRate', 'B/T', 'time'])
        self.__threshold = threshold
        input = Bioinput()
        self.ecg_file = input.file

    def thresholdhr(self):
        print(self.__threshold)
        print(self.__hr_rawdata)
        print(self.ecg_file)

    def change_threshold(self, threshold):
        self.__init__(threshold)

if __name__ == "__main__":
    hr_measure = Biomeasure()
    hr_measure.change_threshold(0.5)
    hr_measure.thresholdhr()

