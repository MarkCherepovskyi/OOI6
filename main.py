from pandas import pandas
import statistics
from sklearn.preprocessing import PowerTransformer
import numpy as np
from sklearn.preprocessing import QuantileTransformer

def main():
    ionosphere = pandas.read_csv("ionosphere.csv")
    mathExps = []
    medians = []
    standardDeviations = []
    recurrentSpivednesses = []
    hmeanes = []
    mads = []
    ranges = []
    despertiones = []
    maxes = []
    mines = []
    centers = []
    normals = []

    # ionosphere.fillna(ionosphere.mean(), inplace=True)
    for i in range(1, 34):
        mathExps.append(mathExpectation(ionosphere[prapare(i)]))
        medians.append(median(ionosphere[prapare(i)]))
        standardDeviations.append(standardDeviation(ionosphere[prapare(i)]))
        recurrentSpivednesses.append(recurrentSpivedness(ionosphere[prapare(i)]))
        hmeanes.append(attrHmean(ionosphere[prapare(i)]))
        mads.append(attrMad(ionosphere[prapare(i)]))
        ranges.append(attrRange(ionosphere[prapare(i)]))
        despertiones.append( despertion(ionosphere[prapare(i)]))
        maxes.append(max(ionosphere[prapare(i)]))
        mines.append(min(ionosphere[prapare(i)]))
        normals.append(normal(ionosphere[prapare(i)]))
        centers.append(center(ionosphere[prapare(i)]))
    print("mathExps: ", mathExps)
    print("medians: ", medians)
    print("standardDeviations: ", standardDeviations)
    print("recurrentSpivednesses: ", recurrentSpivednesses)
    print("hmeanes: ", hmeanes)
    print("ranges: ", ranges)
    print("despertiones: ", despertiones)
    print("maxes: ", maxes)
    print("mines: ", mines)
    print("normals: ", normals)
    print("centers: ", centers)
    print("hyperBalls: ", hyperBallEncode(ionosphere))
    print("hyperCubes: ", hyperCube(ionosphere))

        
def prapare(number):
    if number < 10:
        return "a0" + str(number)
    else:
        return 'a' + str(number)


def mathExpectation(attr):
    mean = statistics.mean(attr)
    return mean


def median(attr):
    mean = statistics.median(attr)
    return mean


def attrHmean(attr):
    return (np.max(attr) + np.min(attr)) / 2



def standardDeviation(attr):
    mean = statistics.mean(attr)
    std_dev = statistics.stdev(attr)  # oбчислення стандартного відхилення від середнього
    return std_dev


def attrMad(attr):
    mean = statistics.mean(attr)
    # обчислення середнього модуля відхилень від середнього
    return statistics.mean(np.absolute(attr - mean))



def attrRange(attr):
    return max(attr) - min(attr)


def despertion(attr):
    return statistics.variance(attr)

def recurrentSpivedness(attr):
    # compute the cumulative mean and median of the sequence
    mean_seq = np.cumsum(attr) / np.arange(1, len(attr) + 1)
    median_seq = np.array([np.median(attr[:i + 1]) for i in range(len(attr))])

    # compute the recurrent ratios of mean and median
    ratios = mean_seq[:-1] / median_seq[:-1]
    return ratios


def center(attr):
   return  attr - attr.mean()

def normal(attr):
    return (attr - attr.min()) / (attr.max() - attr.min())

def hyperBallEncode(attr):
    qt = QuantileTransformer(output_distribution='normal')
    qtData = qt.fit_transform(attr.iloc[:, :-1])
    return qtData


def hyperCube(attr):
    pt = PowerTransformer(method='yeo-johnson')
    ptData = pt.fit_transform(attr.iloc[:, :-1])
    return ptData

if __name__ == "__main__":
    main()
