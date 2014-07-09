########################################################################
#
#    Vision Network - Python source code - file generated by vision
#    Friday 13 April 2007 13:46:37 
#    
#       The Scripps Research Institute (TSRI)
#       Molecular Graphics Lab
#       La Jolla, CA 92037, USA
#
# Copyright: Daniel Stoffler, Michel Sanner and TSRI
#   
# revision: Guillaume Vareille
#  
#########################################################################
#
# $Header: /opt/cvs/python/packages/share1.5/Vision/doc/Examples/matplotlib/Semilogy_net.py,v 1.3 2007/08/29 20:37:16 vareille Exp $
#
# $Id: Semilogy_net.py,v 1.3 2007/08/29 20:37:16 vareille Exp $
#

from traceback import print_exc
## loading libraries ##
from Vision.matplotlibNodes import matplotliblib
masterNet.getEditor().addLibraryInstance(matplotliblib,"Vision.matplotlibNodes", "matplotliblib")

from Vision.StandardNodes import stdlib
masterNet.getEditor().addLibraryInstance(stdlib,"Vision.StandardNodes", "stdlib")

try:
    ## saving node ReadTable ##
    from Vision.StandardNodes import ReadTable
    ReadTable_135 = ReadTable(constrkw = {}, name='ReadTable', library=stdlib)
    masterNet.addNode(ReadTable_135,111,29)
    ReadTable_135.inputPortByName['filename'].widget.set("Data/semilogy_data.dat", run=False)
    ReadTable_135.inputPortByName['sep'].widget.set(",", run=False)
    ReadTable_135.inputPortByName['datatype'].widget.set("float", run=False)
    apply(ReadTable_135.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore ReadTable named ReadTable in network masterNet"
    print_exc()
    ReadTable_135=None

try:
    ## saving node Set Matplotlib options ##
    from Vision.matplotlibNodes import MatPlotLibOptions
    Set_Matplotlib_options_136 = MatPlotLibOptions(constrkw = {}, name='Set Matplotlib options', library=matplotliblib)
    masterNet.addNode(Set_Matplotlib_options_136,251,376)
    Set_Matplotlib_options_136.inputPortByName['matplotlibOptions'].widget.set({'gridcolor': 'black', 'gridOn': 1, 'whichgrid': 'minor', 'gridlinewidth': 0.24999999999999989}, run=False)
except:
    print "WARNING: failed to restore MatPlotLibOptions named Set Matplotlib options in network masterNet"
    print_exc()
    Set_Matplotlib_options_136=None

try:
    ## saving node Semilogy ##
    from Vision.matplotlibNodes import SemilogyNE
    Semilogy_137 = SemilogyNE(constrkw = {}, name='Semilogy', library=matplotliblib)
    masterNet.addNode(Semilogy_137,98,398)
except:
    print "WARNING: failed to restore SemilogyNE named Semilogy in network masterNet"
    print_exc()
    Semilogy_137=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_138 = Index(constrkw = {}, name='Index', library=stdlib)
    masterNet.addNode(Index_138,45,225)
    apply(Index_138.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_138=None

try:
    ## saving node Index ##
    from Vision.StandardNodes import Index
    Index_139 = Index(constrkw = {}, name='Index', library=stdlib)
    masterNet.addNode(Index_139,237,225)
    apply(Index_139.inputPortByName['index'].widget.configure, (), {'max': 1})
    Index_139.inputPortByName['index'].widget.set(1, run=False)
    apply(Index_139.configure, (), {'expanded': True})
except:
    print "WARNING: failed to restore Index named Index in network masterNet"
    print_exc()
    Index_139=None

masterNet.freeze()

## saving connections for network Semilogy ##
if Set_Matplotlib_options_136 is not None and Semilogy_137 is not None:
    try:
        masterNet.connectNodes(
            Set_Matplotlib_options_136, Semilogy_137, "matplotlibOptions", "drawAreaDef", blocking=True)
    except:
        print "WARNING: failed to restore connection between Set_Matplotlib_options_136 and Semilogy_137 in network masterNet"
if ReadTable_135 is not None and Index_138 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_135, Index_138, "data", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between ReadTable_135 and Index_138 in network masterNet"
if ReadTable_135 is not None and Index_139 is not None:
    try:
        masterNet.connectNodes(
            ReadTable_135, Index_139, "data", "data", blocking=True)
    except:
        print "WARNING: failed to restore connection between ReadTable_135 and Index_139 in network masterNet"
if Index_138 is not None and Semilogy_137 is not None:
    try:
        masterNet.connectNodes(
            Index_138, Semilogy_137, "data", "x", blocking=True)
    except:
        print "WARNING: failed to restore connection between Index_138 and Semilogy_137 in network masterNet"
if Index_139 is not None and Semilogy_137 is not None:
    try:
        masterNet.connectNodes(
            Index_139, Semilogy_137, "data", "y", blocking=True)
    except:
        print "WARNING: failed to restore connection between Index_139 and Semilogy_137 in network masterNet"
masterNet.unfreeze()
#masterNet.run()
