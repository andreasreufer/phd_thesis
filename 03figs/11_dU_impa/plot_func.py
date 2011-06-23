#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  return (res.Um[1] - res.U0[1]) / sim.gi.Ered


def filterFunc(sim):
  #return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and (sim.results.mm[2] > 0.1*sim.impb.m )
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. )


#xvar = "vimp"
xvar = "angle"

yaxis = [  1.e-2, 2.1 ]
ylog  = True 
ylbl  = r"$\Delta U / E_{imp}$"
yfmt  = math_formatter
ytik = ( 0.1, 1., 2.)


