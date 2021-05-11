from generate import generateSorted, generatePercentageSorted, generateRandomPercentageSorted, generateReverseSorted, generateRandomSorted
from sorting import shannonSort, shellSort, insertionSort
from testing import isOrdered
from visualization import test
from numpy.polynomial import Polynomial as P
import matplotlib.pyplot as plt
import sympy as sp
from sympy.abc import x

def main():
    sortNames = ("shellSort", "shannonSort", "insertionSort")
    x = [0, 1, 5, 10, 100, 500, 1000, 3000, 5000, 7000, 10000, 15000]
    y = []
    unsorted = []
    sortingAlgos = [shellSort, shannonSort, insertionSort]

    for j in range(0,3):
        for i in range(0,len(x)):
            unsorted = generateRandomPercentageSorted(x[i], 0.8)
            sortedArr, comparisons, assignments = sortingAlgos[j](unsorted)
            y.append(comparisons + assignments)
            
        p = P.fit(x,y,2)
        plt.scatter(x,y)

        modi = str(p)
        modlist = modi.split('+')
        postfix = ["x^2 + ", "x + ", ""]
        for n in range(0,3):
            modlist[n] = "{:.2e}".format(int(modlist[n][:modlist[n].find('.')])) + postfix[n]
            
        legendLabel = sortNames[j] + " - " + ' '.join(modlist)
        plt.plot(*p.linspace(), label = legendLabel)
        plt.legend()
        y = []

    plt.xlabel("size of N")
    plt.ylabel("# of comparisons + assignments")
    plt.title("Runtime of O^2 Sorting Algos Using a 80% Randomly Sorted List")
    plt.gcf().set_size_inches(8,5)
    plt.show()

if __name__ == "__main__":
    main()