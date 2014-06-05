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
import ibmcnx.menu.MenuClass

# Load all jython commands, when they are not loaded
try:
    NewsActivityStreamService.listApplicationRegistrations()
except NameError:
    print "Connections Commands not loaded! Load now: "
    execfile("ibmcnx/loadCnxApps.py")

user = ibmcnx.menu.MenuClass.cnxMenu()
user.AddItem( 'Check External ID (all Apps & Profiles) (cnxMemberCheckExIDByEmail.py)', ibmcnx.functions.cnxMemberCheckExIDByEmail )
user.AddItem( 'Deactivate and Activate a User in one step (cnxMemberDeactAndActByEmail.py)', ibmcnx.functions.cnxMemberDeactAndActByEmail )
user.AddItem( 'Deactivate a User by email address (cnxMemberInactivateByEmail.py)', ibmcnx.functions.cnxMemberInactivateByEmail )
user.AddItem( 'Synchronize ExtID for all Users in all Apps (cnxMemberSyncAllByEXID.py)', ibmcnx.functions.cnxMemberSyncAllByEXID )
user.AddItem( 'Back to Main Menu (cnxmenu.py)', ibmcnx.functions.cnxBackToMainMenu )
user.AddItem( "Exit", ibmcnx.functions.bye )

state = 'True'
while state == 'True':
    user.Show()

    ###########################
    ## Robust error handling ##
    ## only accept int       ##
    ###########################
    ## Wait for valid input in while...not ###
    is_valid=0
    while not is_valid :
        try :
                n = int ( raw_input('Enter your choice [1-6] : ') )

                if n < 7 and n > 0:
				    is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option.") % n
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
   # n = input( "your choice> " )
    user.Do( n - 1 )
