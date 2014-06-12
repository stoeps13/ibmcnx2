######
#  Set the Version Stamp to actual time and date
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Documentation: http://scripting101.stoeps.de
#
#  Version:       2.0
#  Date:          2014-06-04
#
#  License:       Apache 2.0
#

print "\nSet Version Stamp in LotusConnections-config.xml to actual Date and Time\n"

path = raw_input( "Path and Folder where config is temporarily stored: " )

execfile("connectionsConfig.py")
LCConfigService.checkOutConfig(path,AdminControl.getCell())
LCConfigService.updateConfig("versionStamp","")
LCConfigService.checkInConfig(path,AdminControl.getCell())
synchAllNodes()
