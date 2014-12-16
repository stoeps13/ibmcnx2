######
#  Menu for Community Scripts
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

import sys
import os
import ibmcnx.functions
import ibmcnx.menu.MenuClass
import java
from java.lang import String
from java.util import HashSet
from java.util import HashMap

global globdict
globdict = globals()

cfgj2ee = ibmcnx.menu.MenuClass.cnxMenu()
cfgj2ee.AddItem( 'Backup J2EE Roles of all Applications (ibmcnx/config/J2EERoleBackup.py)', ibmcnx.functions.cfgJ2EERoleBackup )
cfgj2ee.AddItem( 'Restore J2EE Roles of all Applications (ibmcnx/config/J2EERoleRestore.py)', ibmcnx.functions.cfgJ2EERoleRestore )
cfgj2ee.AddItem( 'Set J2EE Roles initially (restricted) (ibmcnx/config/J2EERolesRestricted.py)', ibmcnx.functions.cfgJ2EERolesRestricted )
cfgj2ee.AddItem( 'Set J2EE Roles initially (unrestricted) (ibmcnx/config/J2EERolesUnrestricted.py)', ibmcnx.functions.cfgJ2EERolesUnrestricted )
cfgj2ee.AddItem( 'Set J2EE Roles for Moderator Roles (ibmcnx/config/J2EERoleGlobalModerator.py)', ibmcnx.functions.cfgJ2EERoleGlobalModerator )
cfgj2ee.AddItem( 'Set J2EE Role for Metrics Reader (ibmcnx/config/J2EERoleMetricsReader.py)', ibmcnx.functions.cfgJ2EERoleMetricsReader )
cfgj2ee.AddItem( 'Set J2EE Role for Metrics Report Run (ibmcnx/config/J2EERoleMetricsReportRun)', ibmcnx.functions.cfgJ2EERoleMetricsReportRun )
cfgj2ee.AddItem( 'Set J2EE Role for SocialMail (ibmcnx/config/J2EERoleSocialMail)', ibmcnx.functions.cfgJ2EERoleSocialMail )
cfgj2ee.AddItem( 'Back to Main Menu (cnxmenu.py)', ibmcnx.functions.cnxBackToMainMenu )
cfgj2ee.AddItem( "Exit", ibmcnx.functions.bye )

state_cfgj2ee = 'True'
menutitle = "IBM Connections Configuration Tasks"

while state_cfgj2ee == 'True':
    count = len( cfgj2ee.menuitems )
    cfgj2ee.Show( menutitle )

    ###########################
    #  # Robust error handling ##
    #  # only accept int       ##
    ###########################
    ## Wait for valid input in while...not ###
    is_valid_cfg = 0
    while not is_valid_cfg :
        try :
                inputstring = '\tEnter your choice [1-' + str( count ) + ']: '
                n = int ( raw_input( inputstring ) )

                if n <= ( count ) and n > 0:
				    is_valid_cfg = 1    #  # set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option." ) % n
        except ValueError, e :
                print ( "'%s' is not a valid integer." % e.args[0].split( ": " )[1] )
   #  n = input( "your choice> " )
    cfgj2ee.Do( n - 1 )
