'''
Menu for Community Scripts

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       5.0.1
Date:          09/19/2015

License:       Apache 2.0

History:       Changed by Jan Alderlieste
'''

import sys
import os
import ibmcnx.menu.MenuClass
import ibmcnx.functions

#  Only load commands if not initialized directly (call from menu)
# if __name__ == "__main__":
#    execfile( "ibmcnx/loadCnxApps.py" )

global globdict
globdict = globals()


def cnxmenu_cfgtasks():
    execfile('ibmcnx/menu/cfgtasks.py', globdict)


def cnxmenu_cfgj2eetasks():
    execfile('ibmcnx/menu/cfgj2eetasks.py', globdict)


def cnxmenu_useradmin():
    execfile('ibmcnx/menu/useradmin.py', globdict)


def cnxmenu_comm():
    execfile('ibmcnx/menu/comm.py', globdict)


def cnxmenu_checks():
    execfile('ibmcnx/menu/checks.py', globdict)


def cnxmenu_docs():
    execfile('ibmcnx/menu/docs.py', globdict)


def cnxBackToMainMenu():
    execfile('ibmcnx/menu/cnxmenu.py', globdict)

# Check if properties file is present and print warning if not
if ibmcnx.functions.checkPropFile() != 1:
    ibmcnx.functions.propPrintError()

m = ibmcnx.menu.MenuClass.cnxMenu()
m.AddItem('Menu - HCL Connections Configuration Tasks', cnxmenu_cfgtasks)
m.AddItem('Menu - HCL Connections Security Roles Tasks', cnxmenu_cfgj2eetasks)
m.AddItem('Menu - HCL Connections Check Tasks', cnxmenu_checks)
m.AddItem('Menu - HCL Connections User Admin Tasks', cnxmenu_useradmin)
m.AddItem('Menu - HCL Connections Admin Tasks', cnxmenu_comm)
m.AddItem('Menu - HCL Connections Documentation', cnxmenu_docs)
m.AddItem("Exit", ibmcnx.functions.bye)

menutitle = "WebSphere and Connections Administration"
state = 'True'
while state == 'True':
    count = len(m.menuitems)
    m.Show(menutitle)

    ###########################
    #  # Robust error handling ##
    #  # only accept int       ##
    ###########################
    ## Wait for valid input in while...not ###
    is_valid_m = 0
    while not is_valid_m:
        try:
            inputstring = '\tEnter your choice [1-' + str(count) + ']: '
            n = int(raw_input(inputstring))

            if n <= count and n > 0:
                is_valid_m = 1  # set it to 1 to validate input and to terminate the while..not loop
            else:
                print ("'%s' is not a valid menu option.") % n
        except ValueError, e:
            print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
   #  n = input( "your choice> " )
    m.Do(n - 1)
