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

m = ibmcnx.menu.MenuClass.cnxMenu()
m.AddItem( 'Check if all Apps are running (checkAppStatus.py)', ibmcnx.functions.checkAppStatus )
m.AddItem( 'Check Database connections (checkDataSource.py)', ibmcnx.functions.checkDataSource )
m.AddItem( 'Check JVM Heap Sizes (checkJVMHeap.py)', ibmcnx.functions.checkJVMHeap )
m.AddItem( 'Check SystemOut/Err Log Sizes (checkLogFiles.py)', ibmcnx.functions.checkLogFiles )
m.AddItem( 'Check / Show all used ports (checkPorts.py)', ibmcnx.functions.checkPorts )
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
                n = int ( raw_input('Enter your choice [1-7] : ') )

                if n < 8 and n > 0:
				    is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
                else:
                    print ( "'%s' is not a valid menu option.") % n
        except ValueError, e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
   # n = input( "your choice> " )
    m.Do( n - 1 )
