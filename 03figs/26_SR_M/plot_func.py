#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  if res.mm[2] > 0.01*sim.impb.m:
    return (res.mm[2] / sim.impb.m)
  else:
    return nan


def filterFunc(sim):
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and sim.results.mm.shape[0] > 2


xvar = "vimp"
#xvar = "angle"

yaxis = [ -0.1, 1.1 ]
ylog  = False
ylbl  = r"$M_{sr} / M_{imp}$"
yfmt  = math_formatter
#ytik = (-2., -1., 0., 1.)
ytik = (0., 0.2, 0.4, 0.6, 0.8, 1.0)


