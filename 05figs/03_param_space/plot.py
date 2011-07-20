#!/usr/bin/env ipython

import numpy as np
from h5part import H5PartDump
from const_cgs import *

import matplotlib as mp
#mp.use('Agg')
mp.use('macosx')
import matplotlib.pyplot as plt

from matplotlib.patches import Wedge

from plot_helpers import *

#ifile = "summary_m0.txt"
#mflt = 0.2
#mimps = 1.20e27
#rimps = 1.04e9
#vescs = 9.20e5
#lemplt = [2.0, 2.5]
#ofile  = "m0_0.20mimp.pdf" 

#mflt  = 0.15
#mimps = 8.96e26
#rimps = 1.00e9
#vescs = 9.14e5
#lemplt = [1.5, 1.7]
#ofile  = "m0_0.15mimp.pdf" 

#mflt  = 0.1
#mimps = 5.97e26
#rimps = 9.57e8
#vescs = 9.12e5
#lemplt = [1.0, 1.2]
#ofile  = "m0_0.10mimp.pdf" 

#ifile = "summary_i0.txt"
#mflt = 0.2
#mimps = 1.20e27
#rimps = 1.12e9
#vescs = 8.83e5
#lemplt = [2.0, 2.5]
#ofile  = "i0_0.20mimp.pdf" 

ifile = "summary_f0.txt"
#mflt = 0.1
#mimps = 5.97e27
#rimps = 9.20e8
#vescs = 9.31e5
#lemplt = [1.0, 1.2]
#ofile  = "f0_0.10mimp.pdf" 

#mflt = 0.2
#mimps = 1.20e27
#rimps = 9.91e8
#vescs = 9.41e5
#lemplt = [2.0, 2.5]
#ofile  = "f0_0.20mimp.pdf" 

dat = np.loadtxt(ifile)

mtar = dat[:,0]
mimp = dat[:,1]
impa = dat[:,2]
vimp = dat[:,3]
tdat = dat[:,4]
L    = dat[:,5]

mbodyrocktar = dat[:,6]
mbodyrockimp = dat[:,7]
mbodyrock = mbodyrocktar + mbodyrockimp

mdiskrocktar = dat[:,12]
mdiskrockimp = dat[:,13]
mdiskrock = mdiskrocktar + mdiskrockimp

mdiskirontar = dat[:,14]
mdiskironimp = dat[:,15]
mdiskiron = mdiskirontar + mdiskironimp

dltrock = ( ( mdiskrocktar * mbodyrock ) / ( mdiskrock * mbodyrocktar ) ) - 1.

nos = dat.shape[0]

def filt(i):
  return mimp[i] == mflt
  #return True

msize = 0.1

def mark(i):
  return 'o'
  if mimp[i] == 0.2:
    return 'o'
  elif mimp[i] == 0.15:
    return 'd'
  else:
    return 'p'


nofill = [0.5, 0.5, 0.5, 0.0]

fig = plt.figure()

na = plt.axes( [0.0, 0.0, 1.0, 1.0] )
ax = fig.add_subplot(111)

comptxt = "$\mathrm{chondritic}$"

if ifile[8:10] == "i0":
  comptxt = "$\mathrm{icy}$"

if ifile[8:10] == "f0":
  comptxt = "$\mathrm{iron}$"


astr1 = comptxt + "," + \
    (r"$ M_{tar} = %4.2f M_E$, " % mtar[0] ) + \
    (r"$ M_{imp} = %4.2f M_E$" % mflt )
na.text( 0.5, 0.93, astr1, color="black")
na.axis( [0., 1., 0., 1. ] )

cf = []
for i in range(nos):

  if filt(i):
    ax.scatter( impa[i], vimp[i], 300.1,nofill, marker=mark(i) )
    cf = ax.scatter( impa[i], vimp[i], 300.1*(mdiskrock[i]/2.0), dltrock[i], vmin=-1.0, vmax=0., lw=0., marker='o')

    astr1 = (r"    $ %4.2f$" % mdiskrock[i] )
    ax.text( impa[i], vimp[i]-0.008, astr1, color="black", size=10)
    
    astr2 = (r"    $ %4.2f$" % L[i] )
    ax.text( impa[i], vimp[i]+0.007, astr2, color="red", size=10)
    
    astr3 = (r"    $ %4.2f$" % mdiskiron[i] )
    ax.text( impa[i], vimp[i]-0.023, astr3, color="darkblue", size=10)

impr = 46.
vref = 1.35

astr1 = (r'    $M_{disk, Si} [M_L]$' )
ax.text( impr, vref-0.008, astr1, color="black")
    
astr2 = (r'    $L_{bound} [L_{E-m}]$' )
ax.text( impr, vref+0.017, astr2, color="red")

astr3 = (r'    $M_{disk, Fe}  [M_L]$' )
ax.text( impr, vref-0.033, astr3, color="blue")
    
ax.text( 32., 1.45, "$\delta f_T$", color="black", size=16)
    
ax.scatter( impr, vref, 300.1, 'grey', vmin=-1.0, vmax=0., lw=0., marker='o')

ax.set_xlabel(r"$ \theta_{imp}$",color="black")
ax.set_ylabel("$v_{imp} / v_{esc} $",color="black")

impaa = 2.*np.pi*( np.arange( 30., 50. , 0.2) / 360. )
for l in lemplt:
  vrelL = l*lem / ( np.sin( impaa) * rimps*vescs*mimps )
  ax.plot( impaa*(360./(2.*np.pi)), vrelL, 'k--', lw=0.5)
  ax.text( 30., vrelL[0]-0.04, "$%3.1f lem$" % l, color="black",rotation=-40 )

ax.axis( [29., 51, 0.95, 1.5 ] )
#ax.set_axis_bgcolor("black")

ax.xaxis.set_major_formatter(int_formatter)
ax.yaxis.set_major_formatter(math_formatter)

#for txt in ax.xaxis.get_majorticklabels():
#  txt.set_color('white')
#for txt in ax.yaxis.get_majorticklabels():
#  txt.set_color('white')

ax.grid(True)
#for line in ax.xaxis.get_gridlines():
#  line.set_color('w')
#for line in ax.yaxis.get_gridlines():
#  line.set_color('w')

cbax = plt.axes([0.30, 0.85, 0.5, 0.01], frameon=False)

cbar_ticks    = np.arange(-1., 0.2, 0.2)
cbar_tickstxt = []
for x in cbar_ticks:
  cbar_tickstxt.append( "$%3.0f" % (x*100) + "\%$" )

cbar = fig.colorbar(cf, cax=cbax, orientation="horizontal", ticks=cbar_ticks)

cbax.set_xticklabels(cbar_tickstxt)
#for t in cbax.get_xticklabels():
#  t.set_color("w")

fig.savefig(ofile)

