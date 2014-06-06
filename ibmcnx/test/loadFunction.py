
import sys
from java.lang import String
from java.util import HashSet
from java.util import HashMap
import java
import lotusConnectionsCommonAdmin

globdict = globals()

def loadFilesService():
    global globdict
    exec open("filesAdmin.py").read()
