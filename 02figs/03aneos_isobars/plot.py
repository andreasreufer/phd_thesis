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

plt.figure( figsize=(8,4) )

mat1A = pl.loadtxt("T_rho_u_S_cs_at50bars_mat1.txt")
mat2A = pl.loadtxt("T_rho_u_S_cs_at50bars_mat2.txt")
mat4A = pl.loadtxt("T_rho_u_S_cs_at50bars_mat4.txt")
mat5A = pl.loadtxt("T_rho_u_S_cs_at50bars_mat5.txt")

ax1 = plt.subplot(121)
ax1.loglog( mat1A[:,3], mat1A[:,0], 'r-' )
ax1.loglog( mat2A[:,3], mat2A[:,0], '-', color="turquoise" )
ax1.loglog( mat4A[:,3], mat4A[:,0], '-', color="green" )
ax1.loglog( mat5A[:,3], mat5A[:,0], 'b-' )
ax1.text( 200, 2.e4,r'$ 1\mathrm{ bar}$', size=20)
ax1.set_ylabel(r'$T [K]$')


mat1B = pl.loadtxt("T_rho_u_S_cs_at01bars_mat1.txt")
mat2B = pl.loadtxt("T_rho_u_S_cs_at01bars_mat2.txt")
mat4B = pl.loadtxt("T_rho_u_S_cs_at01bars_mat4.txt")
mat5B = pl.loadtxt("T_rho_u_S_cs_at01bars_mat5.txt")

ax2 = plt.subplot(122)
ax2.loglog( mat1B[:,3], mat1B[:,0], 'r-' )
ax2.loglog( mat2B[:,3], mat2B[:,0], '-', color="turquoise" )
ax2.loglog( mat4B[:,3], mat4B[:,0], '-', color="green" )
ax2.loglog( mat5B[:,3], mat5B[:,0], 'b-' )
ax2.text( 200, 2.e4,r'$50\mathrm{bars}$', size=20)


#axs = [ax1, ax2, ax3, ax4]
axs = [ax1, ax2]
for ax in axs:
  ax.grid(True)
  ax.xaxis.set_major_formatter(int_formatter)
  ax.yaxis.set_major_formatter(int_formatter)
  
  ax.set_xlabel(r'$\mathrm{entropy} [J/K/kg]$')
  ax.axis([1.e2, 5.e4, 1.e2, 5.e4])


plt.savefig("out.pdf")
