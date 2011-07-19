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

sdirA = "/Users/areufer/Documents/UniTAPS/gi_sims/m2H/mtar000.900_mimp000.200_impa30.0_vimp1.30/"
sdirB = "/Users/areufer/Documents/UniTAPS/gi_sims/m1H/mtar000.903_mimp000.117_impa45.0_vimp1.05/"

cfileA  = sdirA + "clumps.h5part"
cfileB  = sdirB + "clumps.h5part"


dfileA = sdirA + "dump0022026_T05.0288e+04.h5part"
dfileB = sdirB + "dump0053616_T07.6841e+04.h5part"

axnorm = [-1.6e10, 1.6e10, -0.9e10, 0.9e10]
axzoom = [-3.2e9 , 3.2e9 , -1.8e9 , 1.8e9 ]
axmed  = [-6.4e9 , 6.4e9 , -3.6e9 , 3.6e9 ]

axA = [-1.0e10, 1.0e10, -1.0e10, 1.0e10]
axB = [-1.4e11, 1.4e11, -0.7e11, 0.7e11]
axC = [-0.5e10, 0.5e10, -0.5e10, 0.5e10]

curcfg = cfg_ecc_m
curcfg.xinch = 3.0
curcfg.yinch = 2.0
curcfg.mtar = 0.900
curcfg.mimp = 0.200
curcfg.impa = 30.5
curcfg.vimp = 1.30

curcfg.copy_txt = ""
#curcfg.colorFunc = colorBodyAndMatPaper
#curcfg.colorFunc = colorTemp
#curcfg.Tmin = 300.
#curcfg.Tmax = 12000.
#curcfg.clpr_ls = (0.0, (1,1) )
#curcfg.clp_plotsurf = False
curcfg.parm_vc = [1.1, 1.10]
#curcfg.filt = "negzonly"
curcfg.dpi = 600
curcfg.rmax = 10. * RE
curcfg.scal_min  =   150. / eVinK
curcfg.scal_max  = 12000. / eVinK
curcfg.scal_name = "T"
curcfg.cbar_plot = True
curcfg.cbar_sc   = eVinK
curcfg.cbar_ut   = "K"
curcfg.cbar_fmt  = '%5.0f'
curcfg.cbar_extent = [0.40, 0.10, 0.5, 0.01]
#curcfg.colorFunc = colorScalarLog10
curcfg.colorFunc = colorScalarLinear
curcfg.sctsize   = 0.05


papercolors(curcfg)

#curcfg.ax = axA
#curplot = GIplot(cfg_mat_XY_n)
#curplot.doPlot( dfileA, cfileA, "outA.png" )

#curcfg.postplot = []
#curcfg.parm_vc = [1.1, 1.1]

#curcfg.ax = [-0.1e10, 0.1e10, -0.1e10, 0.1e10]
curplot = GIplot(curcfg)
curplot.doPlot( dfileA, cfileA, "outA.png" )

curplot = GIplot(curcfg)
curplot.doPlot( dfileB, cfileB, "outB.png" )

