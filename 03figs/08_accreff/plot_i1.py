#!/usr/bin/env ipython

import matplotlib as mp
mp.use('Agg')
#mp.use('macosx')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

from sim_admin import SimAdmin, SimParam, SimSetConfig
from simulation import resolvePath
from gi_plot import *
from gi_viz  import GIviz, GIvizConfig
from clumps import ClumpsPlotConfig
from plot_helpers import *
import os
import stat
import time
import numpy as np

#rcParams['text.usetex']=True
mp.rc('text', usetex=True)
mp.rc('text.latex', preamble = '\usepackage{amssymb}, \usepackage{wasysym}')

nan = float('nan')

sscfg = SimSetConfig()
sscfg.name = "i1"
sscfg.dir = "/Users/areufer/Documents/UniTAPS/gi_sims"

simadm = SimAdmin(sscfg)

fig = plt.figure( figsize=(8, 6) )

x0 = 0.12
y0 = 0.10

dx = 0.21
dy = 0.27


params = [ \
    ( SimParam(0.200, 1.000, nan, nan), [2,0] ),
    ( SimParam(0.020, 0.100, nan, nan), [2,1] ),
    ( SimParam(0.002, 0.010, nan, nan), [2,2] )]

bgax = plt.axes( [0.0, 0.0, 1.0, 1.0], frameon=False)
axs = []

def plotFunc(sim):
  res = sim.results
  return (res.mm[1] - sim.tarb.m )/ sim.impb.m
scta = []

for ( sparm, axv ) in params:
  sims = simadm.getSimsByFilter( sparm )
  ax   = plt.axes( [x0 + axv[0]*dx, y0 + axv[1]*dy, dx, dy] )

  sct2arr = ScatterToArray()
  valsims = 0
  for sim in sims:
    x = sim.params.impa
    z = sim.params.vimprel

    if sim.results.valid and ( sim.results.valtmax / sim.tcol > 5. ):
      sct2arr.newPoint(z, x, plotFunc(sim) )
      valsims += 1

  scta = sct2arr

  print len(sims), valsims, axv[0], axv[1]
  (zl, xll, resll) = sct2arr.getArray()

  for i in range(0, len(zl) ):
    vimp = zl[i]
    vimpstr = "$%3.2f v_{esc}$" % vimp
    (col, ls) = getVimpColor(vimp)

    ax.plot( xll[i], resll[i], ls, label=vimpstr, color=col, markersize=6)
  
  ax.axis( [ 0., 90., -2.1, 1.1 ])
  ax.grid(True)
  
  ax.xaxis.set_ticks( (0.,15.,30.,45.,60.,75., 90.) )
  ax.xaxis.set_ticklabels( ("" , "" , "" , "" , "", "", "" ) )
  
  ax.yaxis.set_ticks( (-2., -1., 0., 0.5, 1.0) )
  ax.yaxis.set_ticklabels( ("" , "" , "" , "" , "") )

  axs.append(ax)

for i in (0,):
  axs[i].xaxis.set_major_formatter(int_formatter)
  axs[i].set_xlabel(r"$\theta_{imp}  [^\circ]$")

for i in (0,1,2):
  axs[i].yaxis.set_major_formatter(math_formatter)
  axs[i].set_ylabel(r"$\xi$")


#bgax.text( x0 + 3*dx + 0.07, 0.93, r"$\gamma = 0.10 $" )
bgax.text( x0 + 2*dx + 0.07, 0.93, r"$\gamma = 0.20 $" )
#bgax.text( x0 + 1*dx + 0.07, 0.93, r"$\gamma = 0.35 $" )
#bgax.text( x0 + 0*dx + 0.07, 0.93, r"$\gamma = 0.70 $" )

bgax.text( 0.03, y0 + (0+0.7)*dy, r"$M_{tar} = 1.0 M_{\oplus}$", rotation='vertical')
bgax.text( 0.03, y0 + (1+0.7)*dy, r"$M_{tar} = 0.1 M_{\oplus}$", rotation='vertical')
bgax.text( 0.03, y0 + (2+0.7)*dy, r"$M_{tar} = 0.01 M_{\oplus}$", rotation='vertical')


for i in range(0, len(zl) ):
  vimp = zl[i]
  vimpstr = "$%3.2f$" % vimp
  (col, ls) = getVimpColor(vimp)
  bgax.plot( 99., 99., ls, label=vimpstr, color=col, markersize=6)

bgax.axis( [0., 1., 0., 1.] )

lgfprop = mpl.font_manager.FontProperties(size=10)
bgax.legend(loc=(0.80, 0.06), frameon=False, numpoints=1, ncol=2, columnspacing=0.5, prop=FontProperties(size=8), title=r"$v_{imp} / v_{esc}$", )
bgax.xaxis.set_ticks( () )
bgax.yaxis.set_ticks( () )

plt.savefig("out_i1.pdf")


