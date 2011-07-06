#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results

  if res.Lm.shape[0] > 2:
    return res.Lm[2,2] / sim.gi.Ltot
  else:
    return nan
  

def filterFunc(sim):
  if not ( ( sim.results.valid ) and ( sim.results.valtmax / sim.tcol > 5. ) and sim.params.impa > 5.):
    return False

  if not (hasattr(sim.results, 'Iclmp') and hasattr(sim.results, 'Erotclmp')):
    return False

  if not ( sim.results.mm.shape[0] > 2 ):
    return False

  if (sim.results.mm[2] > 0.1*sim.impb.m ):
    return True
  else:
    return False


#xvar = "vimp"
xvar = "angle"

yaxis = [ 0.9e-3, 1.7]
ylog  = True
ylbl  = r"$[L_{sr} / L_{imp}]_z$"
yfmt  = tex_formatter
ytik = (1.e-3, 1.e-2, 1.e-1, 1.e-0)


