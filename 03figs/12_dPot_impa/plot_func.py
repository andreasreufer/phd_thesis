#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  return (res.Epotm[1] - res.Epot0[1]) / sim.gi.Ered


def filterFunc(sim):
  #return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and (sim.results.mm[2] > 0.1*sim.impb.m )
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. )


#xvar = "vimp"
xvar = "angle"

yaxis = [-2.5, 0.9]
ylog  = False
ylbl  = r"$\Delta E_{pot} / E_{imp}$"
yfmt  = math_formatter
ytik = ( -2., -1., 0.)


