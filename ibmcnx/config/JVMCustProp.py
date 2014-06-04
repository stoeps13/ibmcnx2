######
#  Add Custom Property com.ibm.ws.cache.CacheConfig.filteredStatusCodes to JVM
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

serverNum = WS1.serverNum

for count in range(WS1.serverNum):
    jvm = WS1.jvm[count]
    cell = WS1.cell[count]
    node = WS1.node[count]
    servername = WS1.serverName[count]

    print "%s - %s - %s" % ( cell, node, servername )
    print 'Setting JVM Custom Property'

    AdminConfig.create('Property', jvm, '[[validationExpression ""] [name "com.ibm.ws.cache.CacheConfig.filteredStatusCodes"] [description "Added for js load issue 2014-3-17"] [value "304 404 500 502"] [required "false"]]')

AdminConfig.save()
