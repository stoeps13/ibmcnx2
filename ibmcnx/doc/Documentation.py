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

import sys
import os.path

filename = raw_input( 'Path and Filename to Documentation file: ' )

if (os.path.isfile( filename )):
            answer = raw_input( "File exists, Overwrite, Append or Abort? (O|A|X)" ).lower()
            if answer == "o":
                sys.stdout = open( filename, "w")
            elif answer == "a":
                sys.stdout = open( filename, "a")
            else:
                print "Exit"
                sys.exit()

print '# JVM Settings of all AppServers:'
execfile( 'ibmcnx/doc/JVMSettings.py' )

print '# Used Ports:'
execfile( 'ibmcnx/doc/Ports.py' )

print '# LogFile Settgins:'
execfile( 'ibmcnx/doc/LogFiles.py' )

print '# WebSphere Variables'
execfile( 'ibmcnx/doc/Variables.py' )