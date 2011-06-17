#!/usr/bin/env ipython
import numpy as np
import matplotlib as mp
mp.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.mpl    as mpl
import tables as pt

from gi_plot import *
from h5part import H5PartDump
from plot_helpers import *
from const_cgs import *

plt.rc('savefig', dpi=450)

fig = plt.figure( figsize=(8, 6) )

x0 = 0.12
y0 = 0.10

dx = 0.27
dy = 0.27

axr3rho = plt.axes( [x0 + 0*dx, y0 + 2*dy, dx, dy] )
axr3prs = plt.axes( [x0 + 0*dx, y0 + 1*dy, dx, dy] )
axr3tmp = plt.axes( [x0 + 0*dx, y0 + 0*dy, dx, dy] )

r3ax = (axr3rho, axr3prs, axr3tmp)

axc1rho = plt.axes( [x0 + 1*dx, y0 + 2*dy, dx, dy] )
axc1prs = plt.axes( [x0 + 1*dx, y0 + 1*dy, dx, dy] )
axc1tmp = plt.axes( [x0 + 1*dx, y0 + 0*dy, dx, dy] )

c1ax = (axc1rho, axc1prs, axc1tmp)

axi1rho = plt.axes( [x0 + 2*dx, y0 + 2*dy, dx, dy] )
axi1prs = plt.axes( [x0 + 2*dx, y0 + 1*dy, dx, dy] )
axi1tmp = plt.axes( [x0 + 2*dx, y0 + 0*dy, dx, dy] )

i1ax = (axi1rho, axi1prs, axi1tmp)

strucs = [ \
    ("struc_S_00.100me_S2.40e11_iron0.00_rock1.00_watr0.00.hdf5", r3ax, "b-"), \
    ("struc_S_00.200me_S3.00e11_iron0.00_rock1.00_watr0.00.hdf5", r3ax, "r-"), \
    ("struc_S_00.500me_S3.50e11_iron0.00_rock1.00_watr0.00.hdf5", r3ax, "m-"), \
    
    ("struc_S_00.0020me_S2.40e11_iron0.30_rock0.70_watr0.00.hdf5", c1ax, "r-"), \
    ("struc_S_00.0070me_S2.40e11_iron0.30_rock0.70_watr0.00.hdf5", c1ax, "g-"), \
    ("struc_S_00.0100me_S2.40e11_iron0.30_rock0.70_watr0.00.hdf5", c1ax, "b-"), \
    
    ("struc_S_00.0200me_S2.40e11_iron0.30_rock0.70_watr0.00.hdf5", c1ax, "r-"), \
    ("struc_S_00.0350me_S2.40e11_iron0.30_rock0.70_watr0.00.hdf5", c1ax, "k-"), \
    ("struc_S_00.0700me_S2.40e11_iron0.30_rock0.70_watr0.00.hdf5", c1ax, "g-"), \
    ("struc_S_00.1000me_S2.40e11_iron0.30_rock0.70_watr0.00.hdf5", c1ax, "b-"), \
    
    ("struc_S_00.2000me_S2.40e11_iron0.30_rock0.70_watr0.00.hdf5", c1ax, "r-"), \
    ("struc_S_00.7000me_S2.40e11_iron0.30_rock0.70_watr0.00.hdf5", c1ax, "g-"), \
    ("struc_S_01.0000me_S2.40e11_iron0.30_rock0.70_watr0.00.hdf5", c1ax, "b-"), \
    
    ("struc_S_00.0020me_S2.40e11_iron0.15_rock0.35_watr0.50.hdf5", i1ax, "r-"), \
    ("struc_S_00.0100me_S2.40e11_iron0.15_rock0.35_watr0.50.hdf5", i1ax, "b-"), \
    
    ("struc_S_00.0200me_S2.40e11_iron0.15_rock0.35_watr0.50.hdf5", i1ax, "r-"), \
    ("struc_S_00.1000me_S2.40e11_iron0.15_rock0.35_watr0.50.hdf5", i1ax, "b-"), \

    ("struc_S_00.2000me_S2.40e11_iron0.15_rock0.35_watr0.50.hdf5", i1ax, "r-"), \
    ("struc_S_01.0000me_S2.40e11_iron0.15_rock0.35_watr0.50.hdf5", i1ax, "b-") ]

for (file, axs, prop) in strucs:
  (axrho, axprs, axtmp) = axs
  fh = pt.openFile( "strucs/" + file )
  struc = fh.root

  r = struc.r[:] / RE
  rho = struc.rho[:]
  prs = struc.p[:] / 1.e10
  tmp = struc.T[:] * eVinK
  
  axrho.plot( r, rho, prop, lw=0.4 )
  axrho.plot( r[-1], rho[-1], prop+"|", markersize=20 )
  axprs.semilogy( r, prs, prop, lw=0.4 )
  #axtmp.plot( r, tmp, prop, lw=0.4 )
  axtmp.semilogy( r, tmp, prop, lw=0.4 )
  axtmp.semilogy( r[-1], tmp[-1], prop+"|" )

  fh.close()


axs = [axr3rho, axr3prs, axr3tmp, \
    axc1rho, axc1prs, axc1tmp, \
    axi1rho, axi1prs, axi1tmp ]

for (axrho, axprs, axtmp) in [r3ax, c1ax, i1ax]:
  axrho.xaxis.set_ticks( (0.2, 0.4, 0.6, 0.8, 1.0) )
  axrho.xaxis.set_ticklabels( ("" , "" , "" , "" , "" ) )
  axrho.yaxis.set_ticks( ( 1.0, 3.0, 5.0, 10.) )
  axrho.yaxis.set_ticklabels( ("", "" , "" , "") )
  axrho.grid(True)
  axrho.axis( [0., 1.3, 0.7, 15.] )
  
  axprs.xaxis.set_ticks( (0.2, 0.4, 0.6, 0.8, 1.0) )
  axprs.xaxis.set_ticklabels( ("" , "" , "" , "" , "" ) )
  axprs.yaxis.set_ticks( ( 0.1, 1, 10, 100) )
  axprs.yaxis.set_ticklabels( ("", "" , "" , "") )
  axprs.grid(True)
  axprs.axis( [0., 1.3, 0.02, 500.] )
  
  axtmp.xaxis.set_ticks( (0.2, 0.4, 0.6, 0.8, 1.0) )
  axtmp.xaxis.set_major_formatter(math_formatter)
  axtmp.yaxis.set_ticks( ( 300., 1.e3, 3.0e3, 6.0e3 ) )
  axtmp.yaxis.set_ticklabels( ("", "" , "" , "") )
  axtmp.grid(True)
  axtmp.axis( [0., 1.3, 1.e2, 7.5e3]  )
  
axr3rho.yaxis.set_major_formatter(math_formatter)
axr3rho.set_ylabel(r"$\rho [g/cm^3]$")
axr3prs.yaxis.set_major_formatter(math_formatter)
axr3prs.set_ylabel(r"$p [GPa]$")
axr3tmp.yaxis.set_major_formatter(math_formatter)
axr3tmp.set_ylabel(r"$T [K]$")

axc1tmp.set_xlabel(r"$r [R_E]$")

axr3rho.set_title(r"$\mathrm{silicate}$")
axc1rho.set_title(r"$\mathrm{chondritic}$")
axi1rho.set_title(r"$\mathrm{icy}$")

plt.savefig("out.pdf")


