#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  tertmass = res.mm[3:].sum()
  if tertmass > 0.:
    print sim.params.key, tertmass
    return (tertmass / sim.impb.m)
  else:
    return 1.e-6


def filterFunc(sim):
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and sim.results.mm.shape[0] > 3 and sim.results.mm[3:].sum() > 0.


xvar = "vimp"
#xvar = "angle"

yaxis = [ 1.e-3, 1.1 ]
ylog  = True
#ylbl  = r"$\sum_{i = 3}^N M_i / M_{imp}$"
ylbl  = r"$M_{TR} / M_{imp}$"
yfmt  = tex_formatter
#ytik = (-2., -1., 0., 1.)
#ytik = (0., 0.2, 0.4, 0.6, 0.8, 1.0)
ytik = (1.e-3, 1.e-2, 1.e-1, 1.0)


