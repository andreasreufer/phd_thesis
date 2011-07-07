#!/usr/bin/env ipython

from plot_helpers import *
from numpy import sqrt, pi

nan = float('nan')

def plotFunc(sim):
  res = sim.results
  
  matA = 1
  matB = 5

  #Arelloss =  ( sim.tarb.mmat[matA] - res.mmatm[1,matA] ) / sim.impb.mmat[matA]
  #Brelloss =  ( sim.tarb.mmat[matB] - res.mmatm[1,matB] ) / sim.impb.mmat[matB]

  #accreffA = ( res.mmatm[1,matA] - sim.tarb.mmat[matA] ) / sim.impb.mmat[matA]
  #accreffB = ( res.mmatm[1,matB] - sim.tarb.mmat[matB] ) / sim.impb.mmat[matB]
  
  #return res.mmatm[1,matB] / res.mm[1]

  #  return res.mmatm[2,matB] / res.mm[2]
  
  #return -(accreffA - accreffB)

  return ( res.mmatm[2,matB] / res.mm[2] ) #- ( sim.impb.mmat[matB] / sim.impb.m )

  #if res.mmatm.shape[0] > 1:
  #  return ( res.mmatm[2,matB] / res.mm[2] )# - ( sim.impb.mmat[matB] / sim.impb.m )
  #else:
  #  return nan


def filterFunc(sim):
  res = sim.results
  if not ( sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ) ):
    return False

  if not res.mmatm.shape[0] > 2:
    return False
  
  if res.mm[2] > 0.1*sim.impb.m:
    return True
  else:
    return False

def auxplot(ax):
  pass

xvar = "vimp"
#xvar = "angle"

#yaxis = [ -.30, 1.10 ]
yaxis = [ -0.10, 1.1 ]
ylog  = False
ylbl  = r"$M_{sr, Fe} / M_{lr}$"
yfmt  = math_formatter
#ytik = (0., 0.5 , 1.0 )  
#ytik = (-1.0, -0.5, 0., 0.2)
ytik = ( 0.0, 0.25, 0.5, 0.75, 1.0 )


