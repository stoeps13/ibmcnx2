'''
    Description:
    Author: 	   Christoph Stoettner
    E-Mail: 	   christoph.stoettner@panagenda.com
    Version:     1.0.0
    Date:        2017-05-21
    (C) 2017-05-21 panagenda - all rights reserved

    Install:
    Parameters:
'''

def updateWebContainerProperty(serverName, propName, propValue):
  wc = getWebContainer(serverName)
  updated = 'N'
  try:
      for p in toList(AdminConfig.showAttribute(wc, 'properties')):
        if AdminConfig.showAttribute(p, 'name') == propName:
          AdminConfig.modify(p, [['value', propValue]])
          updated = 'Y'
  except:
        print 'Error in search: ' + serverName
  if updated == 'N':
    setCustomProperties(wc, 'properties', {propName:propValue})
    print propName + ' updated'

def removeWebContainerProperty(serverName, propName):
  wc = getWebContainer(serverName)
  for p in toList(AdminConfig.showAttribute(wc, 'properties')):
    if AdminConfig.showAttribute(p, 'name') == propName:
      AdminConfig.remove(p)

def getWebContainer(serverName):
    serverID = AdminConfig.getid('/Server:' + serverName + '/')
    webContainer = AdminConfig.list('WebContainer', serverID )
    return webContainer

def setCustomProperties (objectName, propertyName, propertyMap):
  propVals = []
  for (key, value) in propertyMap.items():
    propVals.append([["name", key], ["value", value]])
  setObjectProperty(objectName, propertyName, propVals)

def setObjectProperty (objectName, propertyName, propertyValue):
  AdminConfig.modify(objectName, [[propertyName, propertyValue]])

# AdminConfig.create('Property', '(cells/Cell01/nodes/Node01/servers/AppsCluster_server1|server.xml#WebContainer_1464682415269)', '[[validationExpression ""] [name "com.ibm.ws.webcontainer.disablexPoweredBy"] [description "Remove X-Powered-By header"] [value "true"] [required "false"]]')

wasServers = AdminTask.listServers('[-serverType APPLICATION_SERVER]').splitlines()

for wasServer in wasServers:
    serverName = wasServer.split('(')[0]
    try:
        updateWebContainerProperty( serverName, 'com.ibm.ws.webcontainer.disablexPoweredBy', 'true')
    except:
        print 'Error occurred ' + serverName

AdminConfig.save()
