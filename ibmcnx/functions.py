######
#  Functions for IBM Connections Community Scripts
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

def cfgJVMCustProp():
    execfile( 'ibmcnx/config/JVMCustProp.py' )

def checkAppStatus():
    execfile( 'ibmcnx/check/AppStatus.py' )

def checkDataSource():
    execfile( 'ibmcnx/check/DataSource.py' )

def checkJVMHeap():
    execfile( 'ibmcnx/doc/JVMHeap.py' )

def checkLogFiles():
    execfile( 'ibmcnx/doc/LogFiles.py' )

def checkPorts():
    execfile( 'ibmcnx/doc/Ports.py' )

def checkVariables():
    execfile( 'ibmcnx/doc/Variables.py' )

def cnxMemberCheckExIDByEmail():
    execfile( 'ibmcnx/member/CheckExID.py' )

def cnxMemberInactivateByEmail():
    execfile( 'ibmcnx/member/InactivateByEmail.py' )

def cnxMemberDeactAndActByEmail():
    execfile( 'ibmcnx/member/DeactAndActByEmail.py' )

def cnxMemberSyncAllByEXID():
    execfile( 'ibmcnx/member/SyncAllByEXID.py' )

def cnxmenu_cfgtasks():
    execfile( 'ibmcnx/menu/cfgtasks.py',{})

def cnxmenu_useradmin():
    execfile( 'ibmcnx/menu/useradmin.py' )

def cnxmenu_comm():
    execfile( 'ibmcnx/menu/comm.py' )

def cnxmenu_checks():
    execfile( 'ibmcnx/menu/checks.py' )

def cnxBackToMainMenu():
    execfile( 'ibmcnx/menu/cnxmenu.py')

def bye():
    print "bye"
    state = 'false'
    sys.exit( 0 )
