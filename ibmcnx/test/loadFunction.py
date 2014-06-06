
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
    execfile("filesAdmin.py",globdict,locdict)
