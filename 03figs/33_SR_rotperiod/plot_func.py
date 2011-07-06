#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results

  rot = 0.
  if len(res.Erotclmp) > 2:
    rot = 2.*pi*sqrt( res.Iclmp[2] / (2.*res.Erotclmp[2]) ) / 3600.
    print sim.params.key, rot
  else:
    rot = nan
  
  return rot
  

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

  #return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and hasattr(sim.results, 'Iclmp') and hasattr(sim.results, 'Erotclmp') and (sim.results.mm.shape[0] > 1) and (sim.results.mm[2] > 0.1*sim.impb.m )


#xvar = "vimp"
xvar = "angle"

yaxis = [ 2., 50. ]
ylog  = True
ylbl  = r"$ T_{rot} [h]$"
yfmt  = tex_formatter
ytik = ( 3., 6., 12., 24.)


