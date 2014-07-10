import numpy
from periodogram import find_period, rephase, get_phase
import matplotlib.pyplot as plt

def hc(bins, row, col, size):
    hc1 = ((bins[i][j] / size) \
           * numpy.log(sum(bins[m_i][j] / size for m_i in row) \
                       / (bins[i][j] / size))
           for i in row for j in col)
    return numpy.nansum(numpy.fromiter(hc1, dtype="float"))

data = numpy.ma.array(data=numpy.loadtxt('OGLE-LMC-CEP-2147.dat'), mask=None, dtype=float)

#periods = numpy.arange(0.2, 32, 0.001)
periods = numpy.arange(2.4,2.6,0.01)

row = numpy.linspace(0,9,10)
col = numpy.linspace(0,4,5)

entropy = []

for p in periods:
    r = rephase(data, p, 0)

    normalized = numpy.ma.copy(r)
    normalized.T[1] = [ (x[1] - numpy.min(r.T[1]))/(numpy.max(r.T[1])-numpy.min(r.T[1])) for x in normalized]

    bins, binsX, binsY = numpy.histogram2d(normalized.T[0], normalized.T[1], [10,5], [[0,1],[0,1]])
    entropy.append(hc(bins, row, col, len(normalized.T[1])))

print (entropy)
print (periods)

plt.plot(periods,entropy, 'ro')
plt.show()

