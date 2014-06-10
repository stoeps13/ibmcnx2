######
#  Create a file (html or markdown) with the output of
#      - JVMHeap
#      - LogFiles
#      - Ports
#      - Variables
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Documentation: http://scripting101.stoeps.de
#
#  Version:       2.0
#  Date:          2014-06-08
#
#  License:       Apache 2.0
#

# TODO: Create a menu for file selection

import ibmcnx.filehandle
import sys

emp1 = ibmcnx.filehandle.Ibmcnxfile()

sys.stdout = emp1

print '# JVM Settings of all AppServers:'
execfile( 'ibmcnx/doc/JVMSettings.py' )

print '# Used Ports:'
execfile( 'ibmcnx/doc/Ports.py' )

print '# LogFile Settgins:'
execfile( 'ibmcnx/doc/LogFiles.py' )

print '# WebSphere Variables'
execfile( 'ibmcnx/doc/Variables.py' )