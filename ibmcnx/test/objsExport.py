#-----------------------------------------------------------------
# Configuration Objects Export Script
#    Exploits the AdminConfig component of wsadmin to export WAS configuration
#    objects (ie. DataSource, J2CConnetionFactory, etc) to an EXISTING folder.
#    You must specify the folder, the type of objects you want to export
#    and at least the cell they belong to. Optionally, you can further
#    refine the scope by adding a node and a server name.
#    It will produce two files for every exported object:
#
#    1) ObjectID.props, containing header-like information
#    2) ObjectID, containing the actual configuration attributes
#
#    All of the configuration objects matching the imposed criteria
#    will be exported to files. Please don't touch the header info,
#    unless you know what you're doing and/or it's necessary (see
#    objsImport.py), but feel free to modify the attributes as required.
#    Deleting the .props file (or changing its extension) will prevent
#    the object from being imported by the objsImport.py wsadmin script.
#    This is intended to let you easily select which objects to import.
#
#    -------------
#    NOTE: specifying a certain scope will export every object belonging to it
#    and its hierarchically dependent entities. For example, if you only specify
#    a cell, objects defined on its nodes and servers will be exported as well.
#    This behaviour is somehow different w.r.t. what you observe on WAS webconsole
#    (i.e., when you list objects of a certain type, defined on a certain scope).
#    -------------
#    
# Usage:
# wsadmin -lang jython [other wsadmin params] -f objExport.py <export_path> <obj_type> <cell_name> [<node_name> [<server_name>]]
#
# eg.    wsadmin -lang jython -conntype none -f objsExport.py /u/myuserid/export DataSource myCell
#        wsadmin -lang jython -conntype none -f objsExport.py /u/myuserid/export DataSource myCell myNodeA
#        wsadmin -lang jython -conntype none -f objsExport.py /u/myuserid/export DataSource myCell myNodeA myServer1
#        
#        wsadmin -conntype SOAP -host 9.123.45.67 -port 8880 ...
#        wsadmin -conntype RMI -host AIX61 -port 2809 ...
#
# Parameters:
#    export_path: path to the local folder to receive your exported objects
#    obj_type: type of objects to be exported, as defined by AdminConfig.types()
#    cell_name: cell name as it appears in WAS webconsole
#    node_name: node name as it appears in WAS webconsole
#    server_name: server name as it appears in WAS webconsole
#
#-----------------------------------------------------------------

import os, string
from java.io import FileOutputStream
from java.util import Properties
from java.lang import System
from sys import argv, exit


def exportObjectsAttributes(saveDir, objType, cellName, nodeName, srvName):
    
    lineSeparator = System.getProperty("line.separator")
    if saveDir[-1] != "/":
        saveDir = saveDir + "/"
    
    #-------------------------------------------------------------
    # get the object ID corresponding to specified scope
    #-------------------------------------------------------------
    if srvName != "":
        scopeID = AdminConfig.getid("/Cell:" + cellName + "/Node:" + nodeName + "/Server:" + srvName + "/")
    elif nodeName != "":
        scopeID = AdminConfig.getid("/Cell:" + cellName + "/Node:" + nodeName + "/")
    else:
        scopeID = AdminConfig.getid("/Cell:" + cellName + "/")
    
    if scopeID == "" or scopeID == None:
        print "Failed: Could not find the Cell, Node or Server you asked for!"
        return
    
    #-------------------------------------------------------------
    # check if to-be-exported object type requires a provider
    #-------------------------------------------------------------
    typeAttributes = AdminConfig.attributes(objType).split(lineSeparator)
    needsProvider = 0
    for typeAttribute in typeAttributes:
        if typeAttribute.startswith("provider "):
            needsProvider = 1
    
    #-------------------------------------------------------------
    # iterate on all configuration objects of the specified type
    # belonging to the specified scope
    #-------------------------------------------------------------
    for objItem in AdminConfig.list(objType, scopeID).split(lineSeparator):
        if objItem == "" or objItem == None:
            print "Failed: Could not locate any Configuration Object of type " + objType + " in the scope you specified!"
        else:
            
            #-------------------------------------------------------------
            # get current configuration object attributes
            #-------------------------------------------------------------
            props = Properties()
            objItemName = AdminConfig.showAttribute(objItem, "name")
            print "Exporting Item: " + objItemName
            objItemAttributes = AdminConfig.showall(objItem)
            
            #-------------------------------------------------------------
            # build the string needed to obtain parent object ID,
            # this NEED NOT be the same as the specified scope
            #-------------------------------------------------------------
            verticalSlash = objItem.rfind("|")
            openBracket = objItem.rfind("(", 0, verticalSlash)
            parentPath = objItem[openBracket+1:verticalSlash]
            objParentPath = ""
            
            serversInd = parentPath.find("servers")
            if serversInd != -1:
                objParentPath = "Server:" + parentPath[serversInd+8:] + "/"
            else:
                serversInd = len(parentPath)+1
            
            nodesInd = parentPath.find("nodes")
            if nodesInd != -1:
                objParentPath = "Node:" + parentPath[nodesInd+6:serversInd-1] + "/" + objParentPath
            else:
                nodesInd = len(parentPath)+1
            
            cellsInd = parentPath.find("cells")
            if cellsInd != -1:
                objParentPath = "Cell:" + parentPath[cellsInd+6:nodesInd-1] + "/" + objParentPath
            
            objParentPath = "/" + objParentPath
            
            #-------------------------------------------------------------
            # get parent object ID or provider object ID if needed
            #-------------------------------------------------------------
            objItemParent = AdminConfig.getid(objParentPath)
            
            if needsProvider:
                objItemParent = AdminConfig.showAttribute(objItem, "provider")
            
            #-------------------------------------------------------------
            # write .props file and attributes file
            #-------------------------------------------------------------
            props.setProperty("ObjectType", objType)
            props.setProperty("ObjectParent", objItemParent)
            
            tmp = objItem
            if tmp[0] == "\"":
                tmp = tmp[1:]
            if tmp[-1] == "\"":
                tmp = tmp[:-1]
            ind = tmp.rfind(".xml#")
            objItemFileName = tmp[ind+5:-1]
            props.setProperty("ObjectFileName", objItemFileName)
            
            savePropertiesToFile(props, saveDir, objItem, objItemFileName)
            
            objItemFileOutputStream = FileOutputStream(saveDir + objItemFileName)
            objItemFileOutputStream.write(objItemAttributes)
            objItemFileOutputStream.close()


def savePropertiesToFile(props, saveDir, header, objItemRootFileName):
    
    fileOutStream = FileOutputStream(saveDir + objItemRootFileName + ".props")
    props.store(fileOutStream, header)
    fileOutStream.close()


#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------
if len(argv) == 5:
    saveDir = argv[0]
    objType = argv[1]
    cellName = argv[2]
    nodeName = argv[3]
    srvName = argv[4]
    
elif len(argv) == 4:
    saveDir = argv[0]
    objType = argv[1]
    cellName = argv[2]
    nodeName = argv[3]
    srvName = ""

elif len(argv) == 3:
    saveDir = argv[0]
    objType = argv[1]
    cellName = argv[2]
    nodeName = ""
    srvName = ""

else:
    print "\n" + "Failed: Incorrect number of parameters!"
    exit()
    
print ""
exportObjectsAttributes(saveDir, objType, cellName, nodeName, srvName)
