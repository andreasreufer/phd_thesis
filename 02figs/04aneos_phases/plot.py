#!/usr/bin/env ipython
import numpy as np
import matplotlib as mp
mp.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.mpl    as mpl
import tables as pt
import pylab as pl

from gi_plot import *
from h5part import H5PartDump
from plot_helpers import *
from const_cgs import *

plt.rc('savefig', dpi=450)

aneosf = pt.openFile("aneos_tables.hdf5")

#matstr = "01"
#rhoref = 2.65

#matstr = "02"
#rhoref = 1.11

#matstr = "04"
#rhoref = 3.32

matstr = "05"
rhoref = 7.85

UL = eval("aneosf.root.mat" + matstr + "UL")
UH = eval("aneosf.root.mat" + matstr + "UH")
SL = eval("aneosf.root.mat" + matstr + "SL")
SH = eval("aneosf.root.mat" + matstr + "SH")

rhomin = np.power(10., UL.log10rho[0]  )
rhomed = np.power(10., UL.log10rho[-1] )
rhomax = np.power(10., UH.log10rho[-1] )

umin = np.power(10., UL.log10u[0]  ) / 1.e7
umax = np.power(10., UL.log10u[-1] ) / 1.e7

smin = np.power(10., SL.log10S[0] )  / 11605 / 1.e7
smax = np.power(10., SL.log10S[-1] ) / 11605 / 1.e7

phsUL = UL.phase[:,:].astype(np.int8).transpose()
phsUH = UH.phase[:,:].astype(np.int8).transpose()

phsSL = SL.phase[:,:].astype(np.int8).transpose()
phsSH = SH.phase[:,:].astype(np.int8).transpose()


cmap = np.zeros((7,3))

cmap[0] = cnameToRGB("white")      # not valid
cmap[1] = cnameToRGB("grey")       # one-phase
cmap[2] = cnameToRGB("green")      # liq / sol / vap
cmap[4] = cnameToRGB("red")        # solid 
cmap[5] = cnameToRGB("orange")     # solid / liquid
cmap[6] = cnameToRGB("blue")       # liquid

phsULC = cmap[phsUL]
phsUHC = cmap[phsUH]
phsSLC = cmap[phsSL]
phsSHC = cmap[phsSH]


plt.figure( figsize=(11,6) )

ax1L = plt.axes( np.array( [1./11.,1./6.,1./11.,4./6.] ) )
ax1H = plt.axes( np.array( [2./11.,1./6.,3./11.,4./6.] ) )
ax1L.loglog( 2.*rhomin, 0.1*umin, '.' )
ax1H.loglog( 2.*rhomed, 0.1*umin, '.' )
ax1H.vlines(rhoref, umin, umax, linestyle=":")

ax1L.axis([rhomin, rhomed, umin, umax])
ax1L.xaxis.set_ticks( [1.e-10, 0.1] )
ax1H.axis([rhomed, rhomax, umin, umax])
ax1H.yaxis.set_ticks_position("right")

ax1H.set_xlabel(r"$\rho [g/cm^3]$")
ax1L.set_ylabel(r"$u [J/g]$")

ULar = (np.log10( rhomed ) - np.log10( rhomin ))/( np.log10( umax ) - np.log10( umin ))*3.
UHar = (np.log10( rhomax ) - np.log10( rhomed ))/( np.log10( umax ) - np.log10( umin ))*1.
ax1L.imshow(phsULC, extent=[rhomin, rhomed, umin, umax], aspect=ULar)
ax1H.imshow(phsUHC, extent=[rhomed, rhomax, umin, umax], aspect=UHar)



ax2L = plt.axes( np.array( [6./11.,1./6.,1./11.,4./6.] ) )
ax2H = plt.axes( np.array( [7./11.,1./6.,3./11.,4./6.] ) )
ax2L.loglog( 2.*rhomin, 0.1*smin, '.' )
ax2H.loglog( 2.*rhomed, 0.1*smin, '.' )
ax2H.vlines(rhoref, smin, smax, linestyle=":")

ax2L.axis([rhomin, rhomed, smin, smax])
ax2L.xaxis.set_ticks( [1.e-10, 0.1] )
ax2H.axis([rhomed, rhomax, smin, smax])
ax2H.yaxis.set_ticks_position("right")
ax2H.yaxis.set_label_position("right")
ax2H.set_xlabel(r"$\rho [g/cm^3]$")
ax2H.set_ylabel(r'$\mathrm{entropy} [J/g/K]$')

SLar = (np.log10( rhomed ) - np.log10( rhomin ))/( np.log10( smax ) - np.log10( smin ))*3.
SHar = (np.log10( rhomax ) - np.log10( rhomed ))/( np.log10( smax ) - np.log10( smin ))*1.
ax2L.imshow(phsSLC, extent=[rhomin, rhomed, smin, smax], aspect=SLar)
ax2H.imshow(phsSHC, extent=[rhomed, rhomax, smin, smax], aspect=SHar)

axs = [ax1L, ax1H, ax2L, ax2H]
for ax in axs:
  ax.xaxis.set_major_formatter(exponly_formatter)
  ax.yaxis.set_major_formatter(exponly_formatter)

aneosf.close()
plt.savefig("out"+matstr+".png")
