#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  return (res.Epotm[1] - res.Epot0[1] - res.Epot0[2]) / sim.gi.Ered


def filterFunc(sim):
  #return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and (sim.results.mm[2] > 0.1*sim.impb.m )
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and ( sim.results.Epot0.shape[0] > 2 )


#xvar = "vimp"
xvar = "angle"

yaxis = [-1.7, 1.7]
ylog  = False
#ylbl  = r"$E_{pot, lr} - E_{pot, targ} - E_{pot, imp}$"
ylbl  = r"$\Delta E_{pot} / E_{imp}$"
yfmt  = math_formatter
ytik = ( -1., 0., 1.0)


