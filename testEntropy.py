
import numpy
from periodogram import find_period, rephase, get_phase

data = numpy.ma.array(data=numpy.loadtxt('OGLE-2147.dat'), mask=None, dtype=float)

p = find_period(data.T[0], data.T[1], 0.2, 32, 0.001, 0.000001, None)

print (p)

r = rephase(data, p, 0)

row = numpy.linspace(0,9,10)
col = numpy.linspace(0,4,5)

normalized = numpy.ma.copy(r)
normalized.T[1] = [ (x[1] - numpy.min(r.T[1]))/(numpy.max(r.T[1])-numpy.min(r.T[1])) for x in normalized]

bins, binsX, binsY = numpy.histogram2d(normalized.T[0],normalized.T[1], [10,5], [[0,1],[0,1]])

hc1 = [(bins[i][j]/len(normalized.T[1]))*numpy.log(sum(bins[m_i][j]/len(normalized.T[1]) for m_i in row)/(bins[i][j]/len(normalized.T[1]))) for i in row for j in col]

s = numpy.nansum(hc1)
print (s)


