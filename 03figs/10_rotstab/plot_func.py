#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  #ToW = abs(-res.Erotm[1] / res.Epotm[1])
  #ToW = abs(-res.Erotm[1] / sim.gi.Ered)

  ToW = 0.
  if len(res.Erotclmp) > 1:
    ToW = abs(-res.Erotclmp[1] / res.Epotclmp[1])
  else:
    ToW = nan
  
  if ToW  > 10.:
    ToW  = nan

  return ToW
  
  #ToW = abs(-res.Erotm[1] / sim.gi.Ered)
  #ToW = sim.results.Lm[1,2] / sim.gi.Lgraz
  #ToW = sim.results.Lm[1,2] / sim.gi.Ltot
  #ToW = (sim.results.Lm[:,2]).sum() / sim.gi.Ltot
  #ToW = (sim.results.mm[:]).sum() / sim.mtot
  #ToW = sqrt( 2.*res.Erotm[1] / res.Im[1] )
  #if ToW > 100.:
  #  ToW = nan
  #return ToW
  
  #Trot =( 2.*pi*sqrt( res.Im[1] / (2*res.Erotm[1]) ) / 3600. )
  #if Trot > 100.:
  #  Trot = nan
  #return Trot
  
  #return (sim.results.mm[2:] / sim.impb.m).sum()
  #return sim.results.mm[0] / sim.impb.m
  #return (res.mdiskmatm[1,:]).sum() / sim.mtot

  #return 360.*(res.dblvarthetam[2] - 2*sim.gi.vartheta)/(2.*pi)



def filterFunc(sim):
  #return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and (sim.results.mm[2] > 0.1*sim.impb.m )
  return sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) and hasattr(sim.results, 'Epotclmp') and hasattr(sim.results, 'Erotclmp')


#xvar = "vimp"
xvar = "angle"

yaxis = [ 1.e-3, 1.1 ]
ylog  = True
ylbl  = r"$T / |W|_{lr}$"
yfmt  = tex_formatter
ytik = (1.e-3, 1.e-2, 1.e-1)


