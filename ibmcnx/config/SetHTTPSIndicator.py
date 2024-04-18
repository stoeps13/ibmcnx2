'''
Set HTTPSIndicatorHeader for all application server

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       5.0.1
Date:          2024-03-19

License:       Apache 2.0
'''
import ibmcnx.functions

def getAnswer(question):
    answer = ''
    answer = raw_input('\t' + question)
    return answer

WS1 = ibmcnx.appServer.WasServers()

serverNum = WS1.serverNum

headername = getAnswer("What's the name of the HTTP header which shall be set for HttpsIndicatorHeader? ")

for count in range(WS1.serverNum):
    jvm = WS1.jvm[count]
    cell = WS1.cell[count]
    node = WS1.node[count]
    servername = WS1.serverName[count]

    if servername == 'dmgr':
        print "Value not set for %s" % servername
    elif servername == 'nodeagent':
        print "Value not set for %s" % servername
    else:
        print "%s - %s - %s" % (cell, node, servername)
        print 'Setting WebContainer Custom Property'

        server = '"/Server:' + servername + '/"'
        serverId = AdminConfig.getid(server)
        serverWebContainer = AdminConfig.list("WebContainer", serverId )

        attrs = [["name", "HttpsIndicatorHeader"], ["value", headername], ["description", "Important for SSL Offloading"]]

        AdminConfig.create("Property", serverWebContainer, attrs )

ibmcnx.functions.saveChanges()

