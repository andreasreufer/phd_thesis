#!/usr/bin/env ipython

import matplotlib as mp
mp.use('Agg')
import matplotlib.pyplot as plt

from sim_admin import SimAdmin, SimParam, SimSetConfig
from gi_plot import *
from gi_viz  import GIviz, GIvizConfig
from clumps import ClumpsPlotConfig
import os
import numpy as np

nan = float('nan')

sdirA = "/Volumes/SSC/c1/mtar000.010_mimp000.007_impa37.5_vimp3.00/"
sdirB = "/Volumes/SSC/c1/mtar001.000_mimp000.700_impa37.5_vimp3.00/"

cfileA  = sdirA + "clumps_sim.h5part"
cfileB  = sdirB + "clumps_sim.h5part"

#dfileA = sdirA + "dump0026243_T04.3260e+04.h5part"
#dfileB = sdirB + "dump0014357_T03.6121e+04.h5part"

dfileA = sdirA + "dump0020001_T02.3993e+04.h5part"
dfileB = sdirB + "dump0025701_T03.8165e+04.h5part"


axnorm = [-1.6e10, 1.6e10, -0.9e10, 0.9e10]
axzoom = [-3.2e9 , 3.2e9 , -1.8e9 , 1.8e9 ]
axmed  = [-6.4e9 , 6.4e9 , -3.6e9 , 3.6e9 ]

axA = [-1.0e10, 1.0e10, -1.0e10, 1.0e10]
axB = [-1.4e11, 1.4e11, -0.7e11, 0.7e11]

curcfg = cfg_mat_XY_n
curcfg.xinch = 2.0
curcfg.yinch = 2.0
curcfg.mtar = 0.01
curcfg.mimp = 0.007
curcfg.impa = 37.5
curcfg.vimp = 3.00
#curcfg.ax = [-6.4e9 , 3.2e9 , -1.6e9 , 3.2e9 ]
curcfg.copy_txt = ""
curcfg.colorFunc = colorBodyAndMatPaper
curcfg.clpr_ls = (0.0, (1,1) )
curcfg.clp_plotsurf = False
curcfg.parm_vc = [0.3, 0.90]
curcfg.filt = "negzonly"
curcfg.dpi = 600
papercolors(curcfg)

curcfg.ax = axA
curplot = GIplot(cfg_mat_XY_n)
curplot.doPlot( dfileA, cfileA, "outA.png" )

#curcfg.ax = axB
#curplot = GIplot(cfg_mat_XY_n)
#curplot.doPlot( dfileB, cfileB, "outB.png" )

