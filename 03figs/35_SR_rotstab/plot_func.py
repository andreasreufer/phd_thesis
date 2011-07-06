#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results

  ToW = 0.
  if len(res.Erotclmp) > 2:
    ToW = abs(-res.Erotclmp[2] / res.Epotclmp[2])
  else:
    ToW = nan
  
  return ToW
  

def filterFunc(sim):
  if not ( ( sim.results.valid ) and ( sim.results.valtmax / sim.tcol > 5.  )):
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

yaxis = [ 1.e-3, 0.9 ]
ylog  = True
ylbl  = r"$T / |W|_{sr}$"
yfmt  = tex_formatter
ytik = (1.e-3, 1.e-2, 1.e-1)


