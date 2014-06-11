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
import ibmcnx.menu.MenuClass
import ibmcnx.functions

#  Only load commands if not initialized directly (call from menu)
if __name__ == "__main__":
    execfile( "ibmcnx/loadCnxApps.py" )

global globdict
globdict = globals()

def cnxmenu_cfgtasks():
    execfile( 'ibmcnx/menu/cfgtasks.py', globdict )

def cnxmenu_useradmin():
    execfile( 'ibmcnx/menu/useradmin.py', globdict )

def cnxmenu_comm():
    execfile( 'ibmcnx/menu/comm.py', globdict )

def cnxmenu_checks():
    execfile( 'ibmcnx/menu/checks.py', globdict )

def cnxmenu_docs():
    execfile( 'ibmcnx/menu/docs.py', globdict )

def cnxBackToMainMenu():
    execfile( 'ibmcnx/menu/cnxmenu.py', globdict )

m = ibmcnx.menu.MenuClass.cnxMenu()
m.AddItem( 'Menu - IBM Connections Configuration Tasks', cnxmenu_cfgtasks )
m.AddItem( 'Menu - IBM Connections Check Tasks', cnxmenu_checks )
m.AddItem( 'Menu - IBM Connections User Admin Tasks', cnxmenu_useradmin )
m.AddItem( 'Menu - IBM Connections Admin Tasks', cnxmenu_comm )
m.AddItem( 'Menu - IBM Connections Documentation', cnxmenu_docs )
m.AddItem( "Exit", ibmcnx.functions.bye )

state = 'True'
while state == 'True':
    count = len( m.menuitems )
    m.Show()

    ###########################
    #  # Robust error handling ##
    #  # only accept int       ##
    ###########################
    ## Wait for valid input in while...not ###
    is_valid_m = 0
    while not is_valid_m :
        try :
                inputstring = 'Enter your choice [1-' + str( count ) + ']: '
                n = int ( raw_input( inputstring ) )

                if n <= count and n > 0:
                    is_valid_m = 1    #  # set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option." ) % n
        except ValueError, e :
                print ( "'%s' is not a valid integer." % e.args[0].split( ": " )[1] )
   #  n = input( "your choice> " )
    m.Do( n - 1 )
