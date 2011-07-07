#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  return (res.mm[0]) / sim.mtot


def filterFunc(sim):
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and not sim.params.key == "mtar000.100_mimp000.070_impa60.0_vimp1.30"


xvar = "vimp"
#xvar = "angle"

yaxis = [ 0.0009, 1.1]
ylog  = True
ylbl  = r"$M_{ej} / M_{tot}$"
yfmt  = tex_formatter
#ytik = (-2., -1., 0., 1.)
ytik = (1.e-3, 1.e-2, 1.e-1, 1.0)



