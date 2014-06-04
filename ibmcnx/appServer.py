######
#  Classes to work with WebSphere Application Servers
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Documentation: http://scripting101.stoeps.de
#
#  Version:       1.0
#  Date:          2014-06-01
#
#  License:       Apache 2.0
#
#  Get application server names

class WasServers:
    def __init__(self):
        # Get a list of all servers in WAS cell (dmgr, nodeagents, AppServer, webserver)
        self.AllServers = self.getAllServers()
        self.WebServers = self.getWebServers()
        self.AppServers = self.getServersWithoutWeb()
        # self.serverNum, self.jvm, self.cell, self.node, self.serverName = self.getAttrServers()
        self.serverNum, self.jvm, self.cell, self.node, self.serverName = self.getAttrServers()

    def getAllServers(self):
        # get a list of all application servers
        self.servers = AdminTask.listServers().splitlines()
        return self.servers

    def getWebServers(self):
        # get a list of all webservers
        self.webservers = AdminTask.listServers( '[-serverType WEB_SERVER]' ).splitlines()
        return self.webservers

    def getServersWithoutWeb(self):
        self.AppServers = self.AllServers
        for webserver in self.webservers:
            self.AppServers.remove( webserver )
        return self.AppServers

    def getAttrServers(self):
        # get jvm, node, cell from single application server
        srvNum = 0
        jvm = []
        cell = []
        node = []
        servername = []
        for server in self.AppServers:
            srvNum += 1
            javavm = AdminConfig.list( 'JavaVirtualMachine', server )
            jvm.append( javavm )
            srv = server.split( '/' )
            cell.append( srv[1] )
            node.append( srv[3] )
            servername.append( srv[5].split( '|' )[0] )
        self.jvm = jvm
        cell = cell
        node = node
        servername = servername
        # return ( serverNum, jvm, cell, node, serverName )
        return ( srvNum, self.jvm, cell, node, servername )
