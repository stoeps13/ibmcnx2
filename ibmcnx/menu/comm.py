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

# Only load commands if not initialized directly (call from menu)
if __name__ == "__main__":
    execfile("ibmcnx/loadCnxApps.py")

comm = ibmcnx.menu.MenuClass.cnxMenu()
comm.AddItem( 'Reparent/Move Communities (cnxCommunitiesReparenting.py)', ibmcnx.functions.cnxCommunitiesReparenting )
comm.AddItem( 'Back to Main Menu (cnxmenu_comcomm.py)', ibmcnx.functions.cnxBackToMainMenu )
comm.AddItem( "Exit", ibmcnx.functions.bye )

state_comm = 'True'

while state_comm == 'True':
    count = len(comm.menuitems)
    comm.Show()

    ###########################
    ## Robust error handling ##
    ## only accept int       ##
    ###########################
    ## Wait for valid input in while...not ###
    is_valid_comm = 0
    while not is_valid_comm :
        try :
                inputstring = 'Enter your choice [1-' + str(count) +']: '
                n = int ( raw_input( inputstring ) )

                if n <= count and n > 0:
                    is_valid_comm = 1 ## set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option.") % n
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
   # n = input( "your choice> " )
    comm.Do( n - 1 )
