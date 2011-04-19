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
from numpy import log10, power

plt.rc('savefig', dpi=450)
#mp.rc('text', usetex=True)
#plt.rc('text', usetex=True)
plt.rc('text.latex', preamble = '\usepackage{amssymb}, \usepackage{wasysym}')


aneosf = pt.openFile("aneos_tables.hdf5")

#matstr = "01"
#mattitle = r'$\mathrm{M-ANEOS } SiO_2$'
#rhoref = 2650

#matstr = "02"
#mattitle = r'$\mathrm{ANEOS } H_2 O$'
#rhoref = 1110

#matstr = "04"
#mattitle = r'$\mathrm{ANEOS dunite}$'
#rhoref = 3320

matstr = "05"
mattitle = r'$\mathrm{ANEOS iron}$'
rhoref = 7850

UL = eval("aneosf.root.mat" + matstr + "UL")
UH = eval("aneosf.root.mat" + matstr + "UH")
SL = eval("aneosf.root.mat" + matstr + "SL")
SH = eval("aneosf.root.mat" + matstr + "SH")

rhomin = power(10., UL.log10rho[0]  ) * 1.e3
rhomed = power(10., UL.log10rho[-1] ) * 1.e3
rhomax = power(10., UH.log10rho[-1] ) * 1.e3

umin = power(10., UL.log10u[0]  ) / 1.e4
umax = power(10., UL.log10u[-1] ) / 1.e4

smin = power(10., SL.log10S[0] )  / (11605 * 1.e4)
smax = power(10., SL.log10S[-1] ) / (11605 * 1.e4)

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
ax1L.text(rhomin, 1.5*umax, r'$\rho_{min}$')
ax1H.text(rhomed, 1.5*umax, r'$\rho_{med}$')
ax1H.text(rhomax, 1.5*umax, r'$\rho_{max}$')
ax1H.text(rhoref, 1.5*umax, r'$\rho_{0}$')

ax1L.text(power(10., 0.7*(log10(rhomed) + log10(rhomin))), 0.3*umax, r'$100 pts$')
ax1H.text(power(10., 0.5*(log10(rhomax) + log10(rhomed))), 0.3*umax, r'$500 pts$')
ax1L.text(3.*rhomin, power(10., 0.46*(log10(umin) + log10(umax))), r'$1500 pts$', rotation='vertical')


ax1L.axis([rhomin, rhomed, umin, umax])
ax1L.xaxis.set_ticks( [1.e-10, 0.1] )
ax1H.axis([rhomed, rhomax, umin, umax])
ax1H.yaxis.set_ticks_position("right")

ax1H.set_xlabel(r"$\rho [kg/m^3]$")
ax1L.set_ylabel(r"$u [J/kg]$")

ULar = (np.log10( rhomed ) - np.log10( rhomin ))/( np.log10( umax ) - np.log10( umin ))*3.
UHar = (np.log10( rhomax ) - np.log10( rhomed ))/( np.log10( umax ) - np.log10( umin ))*1.
ax1L.imshow(phsULC, extent=[rhomin, rhomed, umin, umax], aspect=ULar)
ax1H.imshow(phsUHC, extent=[rhomed, rhomax, umin, umax], aspect=UHar)


ax2L = plt.axes( np.array( [6./11.,1./6.,1./11.,4./6.] ) )
ax2H = plt.axes( np.array( [7./11.,1./6.,3./11.,4./6.] ) )
ax2L.loglog( 2.*rhomin, 0.1*smin, '.' )
ax2H.loglog( 2.*rhomed, 0.1*smin, '.' )
ax2H.vlines(rhoref, smin, smax, linestyle=":")
ax2L.text(rhomin, 1.5*smax, r'$\rho_{min}$')
ax2H.text(rhomed, 1.5*smax, r'$\rho_{med}$')
ax2H.text(rhomax, 1.5*smax, r'$\rho_{max}$')
ax2H.text(rhoref, 1.5*smax, r'$\rho_{0}$')

ax2L.text(power(10., 0.7*(log10(rhomed) + log10(rhomin))), 0.5*smax, r'$100 pts$')
ax2H.text(power(10., 0.5*(log10(rhomax) + log10(rhomed))), 0.5*smax, r'$500 pts$')
ax2L.text(3.*rhomin, power(10., 0.44*(log10(smin) + log10(smax))), r'$1500 pts$', rotation='vertical')


ax2L.axis([rhomin, rhomed, smin, smax])
ax2L.xaxis.set_ticks( [1.e-10, 0.1] )
ax2H.axis([rhomed, rhomax, smin, smax])
ax2H.yaxis.set_ticks_position("right")
ax2H.yaxis.set_label_position("right")
ax2H.set_xlabel(r"$\rho [kg/m^3]$")
ax2H.set_ylabel(r'$\mathrm{entropy} [J/kg/K]$')

SLar = (np.log10( rhomed ) - np.log10( rhomin ))/( np.log10( smax ) - np.log10( smin ))*3.
SHar = (np.log10( rhomax ) - np.log10( rhomed ))/( np.log10( smax ) - np.log10( smin ))*1.
ax2L.imshow(phsSLC, extent=[rhomin, rhomed, smin, smax], aspect=SLar)
ax2H.imshow(phsSHC, extent=[rhomed, rhomax, smin, smax], aspect=SHar)

axs = [ax1L, ax1H, ax2L, ax2H]
for ax in axs:
  ax.xaxis.set_major_formatter(exponly_formatter)
  ax.yaxis.set_major_formatter(exponly_formatter)

aneosf.close()

bgax = plt.axes( [0., 0., 1., 1.], frameon=False)
bgax.text( 0.4, 0.9, mattitle, size=20)
bgax.axis([0., 1., 0., 1.])
bgax.xaxis.set_ticks( [] )
bgax.yaxis.set_ticks( [] )

bgax.add_patch( mpl.patches.Rectangle( (0.12, 0.07), 0.14, 0.06, color="grey", fill=True ) )
bgax.text( 0.12 + 0.07, 0.10, r'$\mathrm{single phase}$', va="center", ha="center")

bgax.add_patch( mpl.patches.Rectangle( (0.28, 0.07), 0.14, 0.06, color="green", fill=True ) )
bgax.text( 0.28 + 0.07, 0.10, r'$\mathrm{sol. + liq. + vap.}$', va="center", ha="center")

bgax.add_patch( mpl.patches.Rectangle( (0.44, 0.07), 0.14, 0.06, color="red", fill=True ) )
bgax.text( 0.44 + 0.07, 0.10, r'$\mathrm{solid}$', va="center", ha="center")

bgax.add_patch( mpl.patches.Rectangle( (0.60, 0.07), 0.14, 0.06, color="orange", fill=True ) )
bgax.text( 0.60 + 0.07, 0.10, r'$\mathrm{sol. + liq.}$', va="center", ha="center")

bgax.add_patch( mpl.patches.Rectangle( (0.76, 0.07), 0.14, 0.06, color="blue", fill=True ) )
bgax.text( 0.76 + 0.07, 0.10, r'$\mathrm{liquid}$', va="center", ha="center")

plt.savefig("out"+matstr+".png")
