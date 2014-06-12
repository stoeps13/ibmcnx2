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

#  Only load commands if not initialized directly (call from menu)
#if __name__ == "__main__":
#    execfile( "ibmcnx/loadCnxApps.py" )

checks = ibmcnx.menu.MenuClass.cnxMenu()
checks.AddItem( 'Check if all Apps are running (ibmcnx/check/AppStatus.py)', ibmcnx.functions.checkAppStatus )
checks.AddItem( 'Check Database connections (ibmcnx/check/DataSource.py)', ibmcnx.functions.checkDataSource )
checks.AddItem( 'Back to Main Menu (cnxmenu.py)', ibmcnx.functions.cnxBackToMainMenu )
checks.AddItem( "Exit", ibmcnx.functions.bye )

state_checks = 'True'
menutitle = "Check Connectivity"
while state_checks == 'True':
    count = len( checks.menuitems )
    checks.Show( menutitle )

    ###########################
    #  # Robust error handling ##
    #  # only accept int       ##
    ###########################
    ## Wait for valid input in while...not ###
    is_valid_checks = 0
    while not is_valid_checks :
        try :
                inputstring = 'Enter your choice [1-' + str( count ) + ']: '
                n = int ( raw_input( inputstring ) )

                if n <= count and n > 0:
                    is_valid_checks = 1    #  # set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option." ) % n
        except ValueError, e :
                print ( "'%s' is not a valid integer." % e.args[0].split( ": " )[1] )
   #  n = input( "your choice> " )
    checks.Do( n - 1 )
