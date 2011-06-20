#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  return (res.mm[1]) / (sim.mtot)


def filterFunc(sim):
  #return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and (sim.results.mm[2] > 0.1*sim.impb.m )
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. )


xvar = "vimp"
#xvar = "angle"

yaxis = [ -0.05, 1.05 ]
ylog  = False
ylbl  = r"$M_{LR} / M_{tot}$"
yfmt  = math_formatter
ytik = (0.5,1.)


