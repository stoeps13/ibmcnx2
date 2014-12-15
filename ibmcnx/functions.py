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
import ConfigParser

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
        answer_save = raw_input( 'Do you really want to save these changes? ')
        allowed_answer_save = ['yes', 'y', 'ja', 'j']
        if answer_save.lower() in allowed_answer_save:
            print "\n\nSaving changes!\n"
            AdminConfig.save()

            # Synchronize Nodes after Save
            configParser = ConfigParser.ConfigParser()
            configFilePath = r'ibmcnx/ibmcnx.properties'
            configParser.read( configFilePath )
            try:
                autoSyncStatus = configParser.get( 'WebSphere', 'was.autosync' )
            except:
                autoSyncStatus = ''
            print "autoSyncStatus: " + autoSyncStatus
            if ( autoSyncStatus == 'true' ):
                print '\n\nSynchronizing all Nodes!\n\tThis may need some minutes!\n\n'
                synchAllNodes()
            elif ( autoSyncStatus == 'false' ):
                "Please remember to sync your Nodes after ending your session! "
            else:
                answer_sync = raw_input( 'Do you want to synchronize all Nodes? ' )
                allowed_answer_sync = ['yes', 'y', 'ja', 'j']
                if answer_sync.lower() in allowed_answer_sync:
                    print '\n\nSynchronizing all Nodes!\n\tThis may need some minutes!\n\n'
                    synchAllNodes()
                else:
                    print "Please remember to sync your Nodes after ending your session! "
        else:
            print "\nYour changes will not be saved!\n"
    else:
        print 'Nothing to save!'

# Get temporary directory from properties file
def tempPath():
    configParser = ConfigParser.ConfigParser()
    configFilePath = r'ibmcnx/ibmcnx.properties'
    configParser.read( configFilePath )
    try:
        temppath = configParser.get( 'WebSphere','was.temppath' )
    except:
        temppath = ''
    return temppath

# Menu Functions
def cfgDataSource( value ):
    execfile( "ibmcnx/config/DataSources.py" )

def cfgJ2EERoleBackup( value ):
    execfile( "ibmcnx/config/j2ee/RoleBackup.py" )

def cfgJ2EERoleRestore( value ):
    execfile( "ibmcnx/config/j2ee/RoleRestore.py" )

def cfgJ2EERolesRestricted( value ):
    execfile( "ibmcnx/config/j2ee/RoleAllRestricted.py" )

def cfgJ2EERolesUnrestricted( value ):
    execfile( "ibmcnx/config/j2ee/RoleAllUnrestricted.py" )

def cfgJ2EERoleGlobalModerator( value ):
    execfile( "ibmcnx/config/j2ee/RoleGlobalMod.py" )

def cfgJ2EERoleMetricsReader( value ):
    execfile( "ibmcnx/config/j2ee/RoleMetricsReader.py" )

def cfgJ2EERoleMetricsReportRun( value ):
    execfile( "ibmcnx/config/j2ee/RoleMetricsReportRun.py" )

def cfgJ2EERoleSocialMail( value ):
    execfile( "ibmcnx/config/j2ee/RoleSocialMail.py" )

def cfgJVMHeap( value ):
    execfile( "ibmcnx/config/JVMHeap.py" )

def cfgLogFiles( value ):
    execfile( "ibmcnx/config/LogFiles.py" )

def cfgMonitoringPolicy( value ):
    execfile( 'ibmcnx/config/MonitoringPolicy.py' )

def cfgJVMLanguage( value ):
    execfile( 'ibmcnx/config/JVMLanguage.py' )

def cfgJVMCustProp( value ):
    execfile( 'ibmcnx/config/JVMCustProp.py' )

def cfgClusterMembers( value ):
    execfile( 'ibmcnx/config/addNode.py' )

def cfgChgDBHost( value ):
    execfile( 'ibmcnx/config/ChgDBHost.py' )

def checkAppStatus( value ):
    execfile( 'ibmcnx/check/AppStatus.py' )

def checkDataSource( value ):
    execfile( 'ibmcnx/check/DataSource.py' )

def docJVMHeap( value ):
    execfile( 'ibmcnx/doc/JVMHeap.py' )

def docJVMSettings( value ):
    execfile( 'ibmcnx/doc/JVMSettings.py' )

def docLogFiles( value ):
    execfile( 'ibmcnx/doc/LogFiles.py' )

def docPorts( value ):
    execfile( 'ibmcnx/doc/Ports.py' )

def docDataSources( value ):
    execfile( 'ibmcnx/doc/DataSources.py' )

def docVariables( value ):
    execfile( 'ibmcnx/doc/Variables.py' )

def docj2eeroles( value ):
    execfile( 'ibmcnx/doc/j2eeroles.py' )

def cnxBackToMainMenu():
    execfile( 'ibmcnx/menu/cnxmenu.py' )



def bye():
    print "bye"
    state = 'false'
    sys.exit( 0 )
