######
#  Configure JVM Log Files
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

import ibmcnx.appServer

WS1 = ibmcnx.appServer.WasServers()

print "\nChanging the SystemOut & SystemErr log file rotation settings\n"

rollOverType = raw_input( '\tRolloverType (SIZE, BOTH): ' )
maxLogSize = int( raw_input( '\tMax Logfile size in MB (1-50): ' ) )
maxLogHistory = int( raw_input( '\tMax Number of Backup Files (1-200): ' ) )

for count in range(WS1.serverNum):
    try:
        nodename = WS1.node[count]
        servername = WS1.serverName[count]

        if len( nodename ) < 10:
            tab = '\t\t\t'
        elif len( nodename ) > 10 and len( nodename ) < 15:
            tab = '\t\t'
        else:
            tab = '\t'

        # Print Node- and Servername
        print "\tChange log setting for: " + nodename + tab + servername

        # output and errorStream
        systemOut = AdminConfig.showAttribute( server, 'outputStreamRedirect' )
        systemErr = AdminConfig.showAttribute( server, 'errorStreamRedirect' )

        if rollOverType == 'BOTH' or rollOverType.upper() == 'B':
            logSetting = '[[rolloverSize ' + str( maxLogSize ) + '] [rolloverPeriod 24] [maxNumberOfBackupFiles ' + str( maxLogHistory ) + ']]'
        else:
            logSetting = '[[rolloverSize ' + str( maxLogSize ) + '] [maxNumberOfBackupFiles ' + str( maxLogHistory ) + ']]'

        # modify settings for log Size and History
        AdminConfig.modify( systemOut, logSetting )
        AdminConfig.modify( systemErr, logSetting )

    except:
        print "Error on setting Log File Size"

# Save Configuration
AdminConfig.save()
print '\n\n'
