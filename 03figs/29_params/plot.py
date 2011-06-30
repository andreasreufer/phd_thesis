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
import pylab as pl

from numpy import power, pi

from plot_func import *

#rcParams['text.usetex']=True
mp.rc('text', usetex=True)
mp.rc('text.latex', preamble = '\usepackage{amssymb}, \usepackage{wasysym}')

nan = float('nan')

ssname = "c1"
if len(sys.argv) > 1:
  ssname = sys.argv[1]

sscfg = SimSetConfig()
sscfg.name = ssname
sscfg.dir = "/Users/areufer/Documents/UniTAPS/gi_sims"

simadm = SimAdmin(sscfg)

fig = plt.figure( figsize=(8, 6) )

x0 = 0.12
y0 = 0.10

dx = 0.21
dy = 0.27

params = []
if ssname == "c1":
  params = [ \
      ( SimParam(0.200, 1.000, nan, 1.0), [2,0] ),
      ( SimParam(0.700, 1.000, nan, 1.0), [0,0] ),
      ( SimParam(0.010, 0.100, nan, 1.0), [3,1] ),
      ( SimParam(0.020, 0.100, nan, 1.0), [2,1] ),
      ( SimParam(0.035, 0.100, nan, 1.0), [1,1] ),
      ( SimParam(0.070, 0.100, nan, 1.0), [0,1] ),
      ( SimParam(0.002, 0.010, nan, 1.0), [2,2] ),
      ( SimParam(0.007, 0.010, nan, 1.0), [0,2] ) ]

if ssname == "i1":
  params = [ \
      ( SimParam(0.200, 1.000, nan, 1.0), [2,0] ),
      ( SimParam(0.020, 0.100, nan, 1.0), [2,1] ),
      ( SimParam(0.002, 0.010, nan, 1.0), [2,2] ) ]

if ssname == "r3":
  params = [ \
      ( SimParam(0.100, 0.200, nan, 1.0), [0,2] ),
      ( SimParam(0.100, 0.500, nan, 1.0), [1,1] ),
      ( SimParam(0.100, 1.000, nan, 1.0), [2,0] ) ]


bgax = plt.axes( [0.0, 0.0, 1.0, 1.0], frameon=False)
axs = []

zset = {}
for ( sparm, axv ) in params:
  sims = simadm.getSimsByFilter( sparm )
  if len(sims) < 1:
    continue
  
  refsim = sims[0]
  print refsim.params.key
  tarm = refsim.tarb.m
  tarr = refsim.tarb.r
  tarh = refsim.tarb.h

  impm = refsim.impb.m
  impr = refsim.impb.r
  imph = refsim.impb.h

  tarrho = (3.*tarm) / (4.*pi*power(tarr, 3.) )
  imprho = (3.*impm) / (4.*pi*power(impr, 3.) )

  tarnop = refsim.tarb.nop
  impnop = refsim.impb.nop
  tau50  = refsim.tcol * 50. / 3600.

  ax = plt.axes( [x0 + axv[0]*dx, y0 + axv[1]*dy, dx, dy] )
  ax.xaxis.set_ticks(())
  ax.yaxis.set_ticks(())

  
  ax.axis( [0., 1., 0., 1.] )
  
  ax.text( 0.05, 0.85, r"$M_{tar}  $")
  ax.text( 0.30, 0.85, r"$\bar{\rho} = " + ("%3.2f" % tarrho) + " g/cm^3$")
  ax.text( 0.30, 0.73, r"$\bar{h} = " + (latexExp10( '%4.2e' % tarh) ) + " cm$")
  ax.text( 0.30, 0.61, r"$" + str(tarnop) + r"~\mathrm{particles}$" )
  print tarh, (latexExp10( '%4.2e' % tarh) )
  
  ax.text( 0.05, 0.45, r"$M_{imp}  $")
  ax.text( 0.30, 0.45, r"$\bar{\rho} = " + ("%3.2f" % imprho) + " g/cm^3$")
  ax.text( 0.30, 0.33, r"$\bar{h} = " + (latexExp10( '%4.2e' % imph) ) + " cm$")
  ax.text( 0.30, 0.21, r"$" + str(impnop) + r"~\mathrm{particles}$" )
  ax.text( 0.05, 0.05, r"$ 50 \tau_{coll} = " + ('%4.2f' % tau50 ) + " h~~@~v_{esc}$")
  print imph, (latexExp10( '%4.2e' % imph) )
  axs.append(ax)


if ssname == "c1":
  bgax.text( x0 + 3*dx + 0.07, 0.93, r"$\gamma = 0.10 $" )
  bgax.text( x0 + 2*dx + 0.07, 0.93, r"$\gamma = 0.20 $" )
  bgax.text( x0 + 1*dx + 0.07, 0.93, r"$\gamma = 0.35 $" )
  bgax.text( x0 + 0*dx + 0.07, 0.93, r"$\gamma = 0.70 $" )
  bgax.text( 0.03, y0 + (0+0.7)*dy, r"$M_{tar} = 1.0 M_{\oplus}$", rotation='vertical')
  bgax.text( 0.03, y0 + (1+0.7)*dy, r"$M_{tar} = 0.1 M_{\oplus}$", rotation='vertical')
  bgax.text( 0.03, y0 + (2+0.7)*dy, r"$M_{tar} = 0.01 M_{\oplus}$", rotation='vertical')
  
if ssname == "i1":
  bgax.text( x0 + 2*dx + 0.07, 0.93, r"$\gamma = 0.20 $" )
  bgax.text( 0.03, y0 + (0+0.7)*dy, r"$M_{tar} = 1.0 M_{\oplus}$", rotation='vertical')
  bgax.text( 0.03, y0 + (1+0.7)*dy, r"$M_{tar} = 0.1 M_{\oplus}$", rotation='vertical')
  bgax.text( 0.03, y0 + (2+0.7)*dy, r"$M_{tar} = 0.01 M_{\oplus}$", rotation='vertical')
  
if ssname == "r3":
  bgax.text( x0 + 2*dx + 0.07, 0.93, r"$\gamma = 0.10 $" )
  bgax.text( x0 + 1*dx + 0.07, 0.93, r"$\gamma = 0.20 $" )
  bgax.text( x0 + 0*dx + 0.07, 0.93, r"$\gamma = 0.50 $" )
  bgax.text( 0.03, y0 + (0+0.7)*dy, r"$M_{tar} = 1.0 M_{\oplus}$", rotation='vertical')
  bgax.text( 0.03, y0 + (1+0.7)*dy, r"$M_{tar} = 0.5 M_{\oplus}$", rotation='vertical')
  bgax.text( 0.03, y0 + (2+0.7)*dy, r"$M_{tar} = 0.2  M_{\oplus}$", rotation='vertical')
  


bgax.text( 0.03, 0.93, r"$\mathrm{" + sscfg.name + r"}$", size=20)


bgax.axis( [0., 1., 0., 1.] )

legtit = ""
bgax.xaxis.set_ticks( () )
bgax.yaxis.set_ticks( () )

plt.savefig("out_" + ssname + ".pdf")
exit()

