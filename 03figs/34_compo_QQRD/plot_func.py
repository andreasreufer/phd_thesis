#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  return (res.mmatm[1,5]) / (res.mm[1])


def filterFunc(sim):
  #return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and (sim.results.mm[2] > 0.1*sim.impb.m )
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. )


xvar = "vimp"
#xvar = "angle"

yaxis = [ -0.05, 1.05 ]
ylog  = True
ylbl  = r"$M_{LR, Fe} / M_{LR}$"
yfmt  = tex_formatter
ytik = (0.3, 0.4, 0.5, 0.75, 1.)


