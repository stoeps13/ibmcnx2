import ibmcnx.appServer
import ConfigParser

WS1 = ibmcnx.appServer.WasServers()

print "All Servers: %s" % WS1.AllServers
print "Web Servers: %s" % WS1.WebServers
print "App Servers: %s" % WS1.AppServers

print "Server Count: %s" % WS1.serverNum

for count in WS1.serverNum:
    print "JVM: %s" % WS1.jvm[count]

    print "Cell %s: " % self.cell[count]
    print "Node %s: " % self.node[count]
    print "serverName %s: " % self.serverName[count]

configParser = ConfigParser.RawConfigParser()
configFilePath = r'ibmcnx/ibmcnx.properties'
configParser.read(configFilePath)
print "DBUser: %s" % configParser.get('Database','dbUser')
