######
#  Configure Monitoring Policy
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

import ibmcnx.functions
import ibmcnx.appServer

state = ''
while state != ( 'RUNNING' or 'STOPPED' or 'PREVIOUS' ):
    state = raw_input( 'Which state do you want to set? (S|R|P)(STOPPED|RUNNING|PREVIOUS)' ).upper()
    if state == 'R':
        state = 'RUNNING'
        break
    elif state == 'S':
        state = 'STOPPED'
        break
    elif state == 'P':
        state = 'PREVIOUS'
        break
    else:
        continue

WS1 = ibmcnx.appServer.WasServers()

for count in range(WS1.serverNum):
    servername = WS1.serverName[count]
    if servername == 'dmgr':
        print "Value not set for %s" % servername
    elif servername == 'nodeagent':
        print "Value not set for %s" % servername
    else:
        print 'Set nodeRestartState for %s to: %s' % ( servername.split( '(' )[0], state.upper() )
        monitoringPolicy = AdminConfig.list( "MonitoringPolicy", servername )
        AdminConfig.modify( monitoringPolicy, '[[nodeRestartState ' + state.upper() + ']]' )

AdminConfig.save()

print "Synchronizing Nodes"
ibmcnx.functions.synchAllNodes()
