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

import ibmcnx.functions

# Load all jython commands, when they are not loaded
try:
    NewsActivityStreamService.listApplicationRegistrations()
except NameError:
    print "Connections Commands not loaded! Load now: "
    execfile("ibmcnx/loadCnxApps.py")

class cnxMenu_cfgtasks:
    menuitems = []

    # Function to add menuitems
    def AddItem( self, text, function ):
        self.menuitems.append( {'text': text, 'func':function} )

    # Function for printing
    def Show( self ):
        c = 1
        print '\n\tWebSphere and Connections Administration - Checks Tasks'
        print '\t----------------------------------------', '\n'
        for l in self.menuitems:
            print '\t',
            print c, l['text']
            c = c + 1
        print

    def Do( self, n ):
        self.menuitems[n]["func"]()

if __name__ == "__main__":
    m = cnxMenu_cfgtasks()
    m.AddItem( "Configure DataSources (cfgDataSource.py)", ibmcnx.functions.cfgDataSource )
    m.AddItem( 'Backup J2EE Roles of all Applications (cfgJ2EERoleBackup.py)', ibmcnx.functions.cfgJ2EERoleBackup )
    m.AddItem( 'Restore J2EE Roles of all Applications (cfgJ2EERoleRestore.py)', ibmcnx.functions.cfgJ2EERoleRestore )
    m.AddItem( 'Set J2EE Roles initially (restricted) (cfgJ2EERolesRestricted.py)', ibmcnx.functions.cfgJ2EERolesRestricted )
    m.AddItem( 'Set J2EE Roles initially (unrestricted) (cfgJ2EERolesUnrestricted.py)', ibmcnx.functions.cfgJ2EERolesUnrestricted )
    m.AddItem( 'Set J2EE Roles for Moderator Roles (cfgJ2EERoleGlobalModerator.py)', ibmcnx.functions.cfgJ2EERoleGlobalModerator )
    m.AddItem( 'Set J2EE Role for Metrics Reader (cfgJ2EERoleMetricsReader.py)', ibmcnx.functions.cfgJ2EERoleMetricsReader )
    m.AddItem( 'Set J2EE Role for Metrics Report Run (cfgJ2EERoleMetricsReportRun)', ibmcnx.functions.cfgJ2EERoleMetricsReportRun )
    m.AddItem( 'Set J2EE Role for SocialMail (cfgJ2EERoleSocialMail)', ibmcnx.functions.cfgJ2EERoleSocialMail )
    m.AddItem( 'Configure JVM Heap Sizes (cfgJVMHeap.py)', ibmcnx.functions.cfgJVMHeap )
    m.AddItem( 'Set Custom Parameter for Cache Issues in JVM (cfgJVMCustProp.py)', ibmcnx.functions.cfgJVMCustProp )
    m.AddItem( 'Configure SystemOut/Err Log Size (cfgLogFiles.py)', ibmcnx.functions.cfgLogFiles )
    m.AddItem( 'Configure Monitoring Policy (cfgMonitoringPolicy.py)', ibmcnx.functions.cfgMonitoringPolicy )
    m.AddItem( 'Work with Files Policies (cnxFilesPolicies.py)', ibmcnx.functions.cnxFilesPolicies )
    m.AddItem( 'Work with Libraries (cnxLibraryPolicies.py)', ibmcnx.functions.cnxLibraryPolicies )
    m.AddItem( 'Back to Main Menu (cnxmenu.py)', ibmcnx.functions.cnxBackToMainMenu )
    m.AddItem( "Exit", ibmcnx.functions.bye )

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
                n = int ( raw_input('Enter your choice [1-16] : ') )

                if n < 17 and n > 0:
				    is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option.") % n
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
   # n = input( "your choice> " )
    m.Do( n - 1 )
