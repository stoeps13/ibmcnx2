#import ibmcnx.test.loadFunction
import sys
from java.lang import String
from java.util import HashSet
from java.util import HashMap
import java
import lotusConnectionsCommonAdmin

globdict = globals()

def loadFilesService():
    global globdict
    execfile( "filesAdmin.py", globdict )

ibmcnx.test.loadFunction.loadFilesService()

FilesPolicyService.browse( "title", "true", 1, 25 )
