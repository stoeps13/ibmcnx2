import ibmcnx.filehandle
import sys
sys.stdout = open("/tmp/documentation.txt", "w")

print "test"

execfile('ibmcnx/doc/JVMSettings.py' )

