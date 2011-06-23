#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  #return (res.mm[1] - sim.tarb.m) / sim.impb.m
  return (res.mm[1] - sim.tarb.m) / sim.impb.m

def filterFunc(sim):
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. )

def auxplot(ax):
  pass

#xvar = "vimp"
xvar = "angle"

yaxis = [ -2.1, 1.1 ]
ylog  = False
ylbl  = r"$\xi$"
yfmt  = math_formatter
ytik = (-2., -1., 0., 0.5, 1.0)


