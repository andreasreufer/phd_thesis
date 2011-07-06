#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results

  if res.Lm.shape[0] > 1:
    return res.Lm[1,2] / sim.gi.Ltot
  else:
    return nan

def filterFunc(sim):
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and sim.params.impa > 5.


#xvar = "vimp"
xvar = "angle"

yaxis = [ 0.9e-3, 1.7]
ylog  = True
ylbl  = r"$[L_{lr} / L_{imp}]_z$"
yfmt  = tex_formatter
ytik = (1.e-3, 1.e-2, 1.e-1, 1.e-0)


