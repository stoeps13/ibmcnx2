
import sys
from java.lang import String
from java.util import HashSet
from java.util import HashMap
import java
import lotusConnectionsCommonAdmin

globdict = globals()
locdict = locals()

def loadFilesService():
    global globdict
    global locdict
    ldict(globals(),locals())
    execfile("filesAdmin.py",globdict,locdict)
