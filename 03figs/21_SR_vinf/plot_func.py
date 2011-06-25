#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  dvinfvec = res.vinfm[2,:] - res.vinfm[1,:]
  dvinf = np.sqrt( (dvinfvec*dvinfvec).sum() )

  #y = (sim.gi.vinf - dvinf) / sim.gi.vesc
  #if y < 0:
  #  y = nan
  y = dvinf / sim.gi.vesc
  #y = dvinf / sim.gi.vinf
  print y, sim.params.key

  return y
  #return (res.mm[1] - sim.tarb.m) / sim.impb.m


def filterFunc(sim):
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and (sim.results.mm[2] > 0.1*sim.impb.m and sim.results.vinfm.shape[1] > 2)
  #return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. )


#xvar = "vimp"
xvar = "angle"

yaxis = [ 0.9e-1, 5.0]
ylog  = True
ylbl  = r"$v_{+ \infty} / v_{esc}$"
yfmt  = math_formatter
ytik = (1.e-1, 1.e0, 2., 4.)
#ytik = (0.1, 1.)
#ytik = (-2., -1., 0., 1.)


