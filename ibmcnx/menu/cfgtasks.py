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
import ibmcnx.menu.MenuClass
import java
from java.lang import String
from java.util import HashSet
from java.util import HashMap

#  Only load commands if not initialized directly (call from menu)
#if __name__ == "__main__":
#    execfile( "ibmcnx/loadCnxApps.py" )

global globdict
globdict = globals()

cfg = ibmcnx.menu.MenuClass.cnxMenu()
cfg.AddItem( "Configure DataSources (ibmcnx/config/DataSource.py)", ibmcnx.functions.cfgDataSource )
cfg.AddItem( 'Backup J2EE Roles of all Applications (ibmcnx/config/J2EERoleBackup.py)', ibmcnx.functions.cfgJ2EERoleBackup )
cfg.AddItem( 'Restore J2EE Roles of all Applications (ibmcnx/config/J2EERoleRestore.py)', ibmcnx.functions.cfgJ2EERoleRestore )
cfg.AddItem( 'Set J2EE Roles initially (restricted) (ibmcnx/config/J2EERolesRestricted.py)', ibmcnx.functions.cfgJ2EERolesRestricted )
cfg.AddItem( 'Set J2EE Roles initially (unrestricted) (ibmcnx/config/J2EERolesUnrestricted.py)', ibmcnx.functions.cfgJ2EERolesUnrestricted )
cfg.AddItem( 'Set J2EE Roles for Moderator Roles (ibmcnx/config/J2EERoleGlobalModerator.py)', ibmcnx.functions.cfgJ2EERoleGlobalModerator )
cfg.AddItem( 'Set J2EE Role for Metrics Reader (ibmcnx/config/J2EERoleMetricsReader.py)', ibmcnx.functions.cfgJ2EERoleMetricsReader )
cfg.AddItem( 'Set J2EE Role for Metrics Report Run (ibmcnx/config/J2EERoleMetricsReportRun)', ibmcnx.functions.cfgJ2EERoleMetricsReportRun )
cfg.AddItem( 'Set J2EE Role for SocialMail (ibmcnx/config/J2EERoleSocialMail)', ibmcnx.functions.cfgJ2EERoleSocialMail )
cfg.AddItem( 'Configure JVM Heap Sizes (ibmcnx/config/JVMHeap.py)', ibmcnx.functions.cfgJVMHeap )
cfg.AddItem( 'Configure SystemOut/Err Log Size (ibmcnx/config/LogFiles.py)', ibmcnx.functions.cfgLogFiles )
cfg.AddItem( 'Configure Monitoring Policy (ibmcnx/config/MonitoringPolicy.py)', ibmcnx.functions.cfgMonitoringPolicy )
cfg.AddItem( 'Set Custom Parameter for Cache Issues in JVM (ibmcnx/config/JVMCustProp.py)', ibmcnx.functions.cfgJVMCustProp )
cfg.AddItem( 'Back to Main Menu (cnxmenu.py)', ibmcnx.functions.cnxBackToMainMenu )
cfg.AddItem( "Exit", ibmcnx.functions.bye )

state_cfg = 'True'
menutitle = "IBM Connections Configuration Tasks"

while state_cfg == 'True':
    count = len( cfg.menuitems )
    cfg.Show( menutitle )

    ###########################
    #  # Robust error handling ##
    #  # only accept int       ##
    ###########################
    ## Wait for valid input in while...not ###
    is_valid_cfg = 0
    while not is_valid_cfg :
        try :
                inputstring = 'Enter your choice [1-' + str( count ) + ']: '
                n = int ( raw_input( inputstring ) )

                if n <= ( count ) and n > 0:
				    is_valid_cfg = 1    #  # set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option." ) % n
        except ValueError, e :
                print ( "'%s' is not a valid integer." % e.args[0].split( ": " )[1] )
   #  n = input( "your choice> " )
    cfg.Do( n - 1 )
