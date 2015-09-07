######
#  Show the status of all webservers
#
#  Author:        Gwenael Navez
#  Mail:          gwenael.navez@bnpparibasfortis.com
#  Documentation: http://scripting101.stoeps.de
#
#  Version:       5.0
#  Date:          2015-02-23
#
#  License:       Apache 2.0
#
#

import sys
import os

# Function webserversstatus
#
#  Parameters:
#    objname = server properties
#    nodename = node name of the webserver
#    wsname = web server name
#  Output:
#    value = RUNNING  (if webserver is running)
#            UNAVAILABLE (if server is offline)
#


def webserverstatus(cellname, nodename, wsname):
    #objNameString = AdminControl.completeObjectName( 'WebSphere:type=WebServer,name=' +  wsname + ',*')
    objNameString = AdminControl.completeObjectName(
        'WebSphere:type=WebServer,name=WebServer,*')
    invokeparam1 = objNameString
    invokeparam2 = '[' + cellname + ' ' + nodename + ' ' + wsname + ']'
    invokeparam3 = '[java.lang.String java.lang.String java.lang.String]'
    return AdminControl.invoke(invokeparam1, 'ping', invokeparam2, invokeparam3)

# get the webserver list
webservers = AdminTask.listServers('[-serverType WEB_SERVER ]').splitlines()
# create the status tables
runningWebServers = []
stoppedWebServers = []
# get the cell name
cell = AdminControl.getCell()
# for each webservers control the status
for webserver in webservers:
    nodename = webserver.split('/')
    nodename = nodename[3]
    cellname = webserver.split('/')
    cellname = cellname[1]
    webserverName = webserver.split('/')
    webserverName = webserverName[5]
    webserverName = webserverName.split('|')
    webserverName = webserverName[0]
    objNameString = AdminControl.completeObjectName(
        'WebSphere:type=WebServer,name=' + webserverName + ',*')
    if webserverstatus(cellname, nodename, webserverName) == 'RUNNING':
        wStatus = 'running'
        runningWebServers.append(webserverName)
    else:
        wStatus = 'stopped'
        stoppedWebServers.append(webserverName)
runningWebServers.sort()
stoppedWebServers.sort()
print ' '
print 'Getting status of all web servers....'
print ''
print '\tRUNNING WEBSERVERS: \n'
for web in runningWebServers:
    print '\t\t' + web

print ''
print '\tSTOPPED WEBSERVERS: \n'
for web in stoppedWebServers:
    print '\t\t' + web
