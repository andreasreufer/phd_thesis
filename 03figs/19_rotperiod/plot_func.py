#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results

  rot = 0.
  if len(res.Erotclmp) > 1:
    rot = 2.*pi*sqrt( res.Iclmp[1] / (2.*res.Erotclmp[1]) ) / 3600.
  else:
    rot = nan
  
  return rot
  

def filterFunc(sim):
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and hasattr(sim.results, 'Iclmp') and hasattr(sim.results, 'Erotclmp')


#xvar = "vimp"
xvar = "angle"

yaxis = [ 2., 50. ]
ylog  = True
ylbl  = r"$ T_{rot} [h]$"
yfmt  = tex_formatter
ytik = ( 3., 6., 12., 24.)


