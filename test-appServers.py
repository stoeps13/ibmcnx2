import ibmcnx.appServer
import ConfigParser

WS1 = ibmcnx.appServer.WasServers()

print "All Servers: %s" % WS1.AllServers
print "Web Servers: %s" % WS1.WebServers
print "App Servers: %s" % WS1.AppServers

print "Server Count: %s" % WS1.serverNum

for count in range(WS1.serverNum):
    print "JVM: %s" % WS1.jvm[count]

    print "Cell %s: " % WS1.cell[count]
    print "Node %s: " % WS1.node[count]
    print "serverName %s: " % WS1.serverName[count]

configParser = ConfigParser.ConfigParser()
configFilePath = r'ibmcnx/ibmcnx.properties'
configParser.read(configFilePath)
print "DBUser: %s" % configParser.get('Database','dbUser')
