######
#  Functions for IBM Connections Community Scripts
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Documentation: http://scripting101.org
#
#  Version:       2.0
#  Date:          2014-06-04
#
#  License:       Apache 2.0
#
#  Collection of functions

import os
import sys

# Function to get the DataSource ID
def getDSId( dbName ):
    try:
        DSId = AdminConfig.getid( '/DataSource:' + dbName + '/' )
        return DSId
    except:
        print "Error when getting the DataSource ID!"
        pass

# Function to check for a filepath and create it, when not present
def checkBackupPath( path ) :
    try :
        os.makedirs( path )
    except OSError :
        if not os.path.isdir( path ) :
            raise

# Function for Set Roles Script
def getAdmin( adminvar ):
    # function to ask for adminusers
    # return a list with admins
    # function is called for each admin type and each admin group type
    admins = []
    admin = ''
    adminstring = ''
    admindict = {
                 'connwasadmin':'Local WebSphere AdminUser',
                 'connadmin':'LDAP WebSphere and Connections AdminUser (searchAdmin)',
                 'connmoderators':'Moderator User',
                 'connmetrics':'Metrics Admin',
                 'connmobile':'Mobile Administrators',
                 'connadmingroup':'LDAP Admin Group',
                 'connmoderatorgroup':'Moderators Admin Group',
                 'connmetricsgroup':'Metrics Admin Group',
                 'connmobilegroup':'Mobile Admin Group'
    }
    print 'Type 0 when finished, uid is case sensitiv!'
    while admin != "0":
        admin = raw_input( 'Type uid for ' + admindict[adminvar] + ': ' )
        if admin != '0' and admin != '':
            admins.append( admin )
    adminstring = '|'.join( admins )
    print adminstring
    return adminstring

# Function to synchronize all Nodes
def synchAllNodes():
    nodelist = AdminTask.listManagedNodes().splitlines()
    cell = AdminControl.getCell()
    for nodename in nodelist :
        print "Syncronizing node " + nodename + " -",
        try:
            repo = AdminControl.completeObjectName( 'type=ConfigRepository,process=nodeagent,node=' + nodename + ',*' )
            AdminControl.invoke( repo, 'refreshRepositoryEpoch' )
            sync = AdminControl.completeObjectName( 'cell=' + cell + ',node=' + nodename + ',type=NodeSync,*' )
            AdminControl.invoke( sync , 'sync' )
            print " completed "
        except:
            print " error"

    print ""

# Function to save changes only when necessary
def saveChanges():
    if (AdminConfig.hasChanges()):
        print "\n\nSaving changes!\n"
        AdminConfig.save()
        print '\n\nSynchronizing all Nodes!\n\tThis may need some minutes!\n\n'
        ibmcnx.functions.synchAllNodes()
    else:
        print 'Nothing to save!'

# Menu Functions
def cfgDataSource():
    execfile( "ibmcnx/config/DataSources.py" )

def cfgJ2EERoleBackup():
    execfile( "ibmcnx/config/j2ee/RoleBackup.py" )

def cfgJ2EERoleRestore():
    execfile( "ibmcnx/config/j2ee/RoleRestore.py" )

def cfgJ2EERolesRestricted():
    execfile( "ibmcnx/config/j2ee/RoleAllRestricted.py" )

def cfgJ2EERolesUnrestricted():
    execfile( "ibmcnx/config/j2ee/RoleAllUnrestricted.py" )

def cfgJ2EERoleGlobalModerator():
    execfile( "ibmcnx/config/j2ee/RoleGlobalMod.py" )

def cfgJ2EERoleMetricsReader():
    execfile( "ibmcnx/config/j2ee/RoleMetricsReader.py" )

def cfgJ2EERoleMetricsReportRun():
    execfile( "ibmcnx/config/j2ee/RoleMetricsReportRun.py" )

def cfgJ2EERoleSocialMail():
    execfile( "ibmcnx/config/j2ee/RoleSocialMail.py" )

def cfgJVMHeap():
    execfile( "ibmcnx/config/JVMHeap.py" )

def cfgLogFiles():
    execfile( "ibmcnx/config/LogFiles.py" )

def cfgMonitoringPolicy():
    execfile( 'ibmcnx/config/MonitoringPolicy.py' )

def cfgJVMLanguage():
    execfile( 'ibmcnx/config/JVMLanguage.py' )

def cfgJVMCustProp():
    execfile( 'ibmcnx/config/JVMCustProp.py' )

def cfgClusterMembers():
    execfile( 'ibmcnx/config/addNode.py' )

def cfgChgDBHost():
    execfile( 'ibmcnx/config/ChgDBHost.py' )

def checkAppStatus():
    execfile( 'ibmcnx/check/AppStatus.py' )

def checkDataSource():
    execfile( 'ibmcnx/check/DataSource.py' )

def docJVMHeap():
    execfile( 'ibmcnx/doc/JVMHeap.py' )

def docJVMSettings():
    execfile( 'ibmcnx/doc/JVMSettings.py' )

def docLogFiles():
    execfile( 'ibmcnx/doc/LogFiles.py' )

def docPorts():
    execfile( 'ibmcnx/doc/Ports.py' )

def docDataSources():
    execfile( 'ibmcnx/doc/DataSources.py' )

def docVariables():
    execfile( 'ibmcnx/doc/Variables.py' )

def docj2eeroles():
    execfile( 'ibmcnx/doc/j2eeroles.py' )

def cnxBackToMainMenu():
    execfile( 'ibmcnx/menu/cnxmenu.py' )



def bye():
    print "bye"
    state = 'false'
    sys.exit( 0 )
