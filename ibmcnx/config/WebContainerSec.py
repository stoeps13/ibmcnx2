'''
    Description:   Set property to disable Websphere header x-powered-by
    Author: 	   Christoph Stoettner
    E-Mail: 	   christoph.stoettner@panagenda.com
    Version:       1.0.0
    Date:          2023-09-15
    (C) Christoph Stoettner

    Install:
    Parameters:
'''
import ibmcnx.functions

def updateWebContainerProperty(serverName, propName, propValue):
  serverID = AdminConfig.getid('/Server:' + serverName + '/')
  wc = AdminConfig.list('WebContainer', serverID )
  updated = 'N'
  try:
      for p in AdminConfig.showAttribute(wc, 'properties').split('[')[1].split(']')[0].split():
        if AdminConfig.showAttribute(p, 'name') == propName:
          AdminConfig.modify(p, [['value', propValue]])
          print(propName + ' modified')
          updated = 'Y'
  except:
        print 'Error in search: ' + serverName
  if updated == 'N':
    #setCustomProperties(wc, 'properties', {propName:propValue})
    propVals = []
    propVals.append([["name", propName], ["value", propValue]])
    AdminConfig.modify(wc, [['properties', propVals]])
    print propName + ' added'

def removeWebContainerProperty(serverName, propName):
  serverID = AdminConfig.getid('/Server:' + serverName + '/')
  wc = AdminConfig.list('WebContainer', serverID )
  for p in AdminConfig.showAttribute(wc, 'properties').split('[')[1].split(']')[0].split():
    if AdminConfig.showAttribute(p, 'name') == propName:
      print(p)
      AdminConfig.remove(p)

def setCustomProperties (objectName, propertyName, propertyMap):
  propVals = []
  for (key, value) in propertyMap.items():
    propVals.append([["name", key], ["value", value]])
  setObjectProperty(objectName, propertyName, propVals)

def setObjectProperty (objectName, propertyName, propertyValue):
  AdminConfig.modify(objectName, [[propertyName, propertyValue]])

wasServers = AdminTask.listServers('[-serverType APPLICATION_SERVER]').splitlines()

for wasServer in wasServers:
    serverName = wasServer.split('(')[0]
    try:
        updateWebContainerProperty( serverName, 'com.ibm.ws.webcontainer.disablexPoweredBy', 'true')
        # removeWebContainerProperty( serverName, 'com.ibm.ws.webcontainer.disablexPoweredBy')
    except:
        print 'Error occurred ' + serverName

print '\n'
ibmcnx.functions.saveChanges()
print '\n'
