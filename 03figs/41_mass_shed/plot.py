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

sdir = "/Volumes/SSC/c1/mtar001.000_mimp000.700_impa89.0_vimp1.00/"

cfile  = sdir + "clumps_sim.h5part"

dfileA = sdir + "dump0013971_T02.2945e+03.h5part"
dfileB = sdir + "dump0024574_T02.2945e+04.h5part"
dfileC = sdir + "dump0057497_T01.1472e+05.h5part"

axnorm = [-1.6e10, 1.6e10, -0.9e10, 0.9e10]
axzoom = [-3.2e9 , 3.2e9 , -1.8e9 , 1.8e9 ]
axmed  = [-6.4e9 , 6.4e9 , -3.6e9 , 3.6e9 ]

axA = [-1.0e10, 1.0e10, -1.0e10, 1.0e10]
axB = [-1.4e11, 1.4e11, -0.7e11, 0.7e11]
axC = [-0.5e10, 0.5e10, -0.5e10, 0.5e10]

curcfg = cfg_mat_XY_n
curcfg.xinch = 2.0
curcfg.yinch = 2.0
curcfg.mtar = 1.00
curcfg.mimp = 0.70 
curcfg.impa = 89.0
curcfg.vimp = 1.00
curcfg.copy_txt = ""
curcfg.colorFunc = colorBodyAndMatPaper
curcfg.clpr_ls = (0.0, (1,1) )
curcfg.clp_plotsurf = False
curcfg.parm_vc = [0.3, 0.90]
curcfg.filt = "negzonly"
curcfg.dpi = 600

papercolors(curcfg)

curcfg.xinch = 2.0
curcfg.yinch = 1.5
curcfg.ax = [-3.0e10, 1.0e10, -1.0e10, 2.0e10]
curplot = GIplot(cfg_mat_XY_n)
curplot.doPlot( dfileC, cfile, "outC.png" )

curcfg.xinch = 1.0
curcfg.yinch = 1.0
curcfg.parm_vc = [1.1, 1.1]

curcfg.ax = [-0.5e10, 0.5e10, -0.5e10, 0.5e10]
curplot = GIplot(cfg_mat_XY_n)
curplot.doPlot( dfileA, cfile, "outA.png" )

curcfg.ax = [-0.5e10, 0.5e10, -0.5e10, 0.5e10]
#curcfg.ax = [-1.0e10, 1.0e10, -1.0e10, 1.0e10]
curplot = GIplot(cfg_mat_XY_n)
curplot.doPlot( dfileB, cfile, "outB.png" )


