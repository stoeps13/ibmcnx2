######
#  Menu for Community Scripts
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
#  History:       Changed by Jan Alderlieste

import sys
import os
import ibmcnx.functions

# Only load commands if not initialized directly (call from menu)
if __name__ == "__main__":
    execfile("ibmcnx/loadCnxApps.py")

class cnxMenu:
    menuitems = []

    # Function to add menuitems
    def AddItem( self, text, function ):
        self.menuitems.append( {'text': text, 'func':function} )

    # Function for printing
    def Show( self ):
        c = 1
        print '\n\tWebSphere and Connections Administration'
        print '\t----------------------------------------', '\n'
        for l in self.menuitems:
            print '\t',
            print c, l['text']
            c = c + 1
        print

    def Do( self, n ):
        self.menuitems[n]["func"]()



def cfgJ2EERoleBackup():
    execfile( "cfgJ2EERoleBackup.py" )

def cfgJ2EERoleRestore():
    execfile( "cfgJ2EERoleRestore.py" )

def cfgJ2EERolesRestricted():
    execfile( "cfgJ2EERolesRestricted.py" )

def cfgJ2EERolesUnrestricted():
    execfile( "cfgJ2EERolesUnrestricted.py" )

def cfgJ2EERoleGlobalModerator():
    execfile( "cfgJ2EERoleGlobalModerator.py" )

def cfgJ2EERoleMetricsReader():
    execfile( "cfgJ2EERoleMetricsReader.py" )

def cfgJ2EERoleMetricsReportRun():
    execfile( "cfgJ2EERoleMetricsReportRun.py" )

def cfgJ2EERoleSocialMail():
    execfile( "cfgJ2EERoleSocialMail.py" )

def cfgJVMHeap():
    execfile( "cfgJVMHeap.py" )

def cfgLogFiles():
    execfile( "cfgLogFiles.py" )

def cfgMonitoringPolicy():
    execfile( 'cfgMonitoringPolicy.py' )

def cfgJVMCustProp():
    execfile( 'cfgJVMCustProp.py' )

def checkAppStatus():
    execfile( 'checkAppStatus.py' )

def checkDataSource():
    execfile( 'checkDataSource.py' )

def checkJVMHeap():
    execfile( 'checkJVMHeap.py' )

def checkLogFiles():
    execfile( 'checkLogFiles.py' )

def checkPorts():
    execfile( 'checkPorts.py' )

def checkVariables():
    execfile( 'checkVariables.py' )

def cnxFilesPolicies():
    execfile( 'cnxFilesPolicies.py' )

def cnxLibraryPolicies():
    execfile( 'cnxLibraryPolicies.py' )

def cnxMemberCheckExIDByEmail():
    execfile( 'cnxMemberCheckExIDByEmail.py' )

def cnxMemberInactivateByEmail():
    execfile( 'cnxMemberInactivateByEmail.py' )

def cnxMemberDeactAndActByEmail():
    execfile( 'cnxMemberDeactAndActByEmail.py' )

def cnxMemberSyncAllByEXID():
    execfile( 'cnxMemberSyncAllByEXID.py' )

def cnxCommunitiesReparenting():
    execfile( 'cnxCommunitiesReparenting.py' )

def cnxmenu_cfgtasks():
	execfile( 'ibmcnx/menu/cnxmenu_cfgtasks.py' )

def cnxmenu_useradmin():
	execfile( 'ibmcnx/menu/cnxmenu_useradmin.py' )

def cnxmenu_comm():
	execfile( 'ibmcnx/menu/cnxmenu_comm.py' )

def cnxmenu_checks():
	execfile( 'ibmcnx/menu/cnxmenu_checks.py' )

def bye():
    print "bye"
    state = 'false'
    sys.exit( 0 )

if __name__ == "__main__":
    m = cnxMenu()
    m.AddItem( 'Menu - IBM Connections Configuration Tasks', cnxmenu_cfgtasks )
    m.AddItem( 'Menu - IBM Connections/WebSphere Check Tasks', cnxmenu_checks )
    m.AddItem( 'Menu - IBM Connections User Admin Tasks', cnxmenu_useradmin )
    m.AddItem( 'Menu - IBM Connections Community Admin Tasks', cnxmenu_comm )
    m.AddItem( "Exit", bye )

state = 'True'
while state == 'True':
    m.Show()

    ###########################
    ## Robust error handling ##
    ## only accept int       ##
    ###########################
    ## Wait for valid input in while...not ###
    is_valid=0
    while not is_valid :
        try :
                n = int ( raw_input('Enter your choice [1-5] : ') )

                if n < 6 and n > 0:
				    is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option.") % n
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
   # n = input( "your choice> " )
    m.Do( n - 1 )
