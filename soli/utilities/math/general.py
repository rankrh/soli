import numpy as np


phi = (1 + np.sqrt(5)) / 2

def getRatio(*numbers):
    if len(numbers) > 2:
        return
    print(numbers[0] / numbers[1])
    return max(numbers) / min(numbers)

def getDivisorsAndRemainders(x):
    
    lowDivisors = [f for f in range(1, int(np.sqrt(x) + 1))]
    return np.array([(f, int(x / f), x % f) for f in lowDivisors])

def getFactors(x):
    lowFactors = [f for f in range(1, int(np.sqrt(x) + 1)) if x % f == 0]
    return np.array([(f, int(x / f)) for f in lowFactors])

def getGoldenestFactor(factors):
    ratios = {factor: abs(phi - getRatio(*factor)) for factor in factors}
    print(ratios)
    return min(ratios, key=ratios.get)

