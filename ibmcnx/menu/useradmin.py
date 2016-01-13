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
import ibmcnx.functions
import ibmcnx.menu.MenuClass

# Only load commands if not initialized directly (call from menu)
# if __name__ == "__main__":
#    execfile("ibmcnx/loadCnxApps.py")

global globdict
globdict = globals()


def cnxMemberCheckExIDByEmail():
    execfile('ibmcnx/member/CheckExId.py', globdict)


def cnxMemberInactivateByEmail():
    execfile('ibmcnx/member/InactivateByEmail.py', globdict)


def cnxMemberDeactAndActByEmail():
    execfile('ibmcnx/member/DeactAndActByEmail.py', globdict)


def cnxMemberInactivateByUid():
    execfile('ibmcnx/member/InactivateByUid.py', globdict)


def cnxMemberSyncAllByEXID():
    execfile('ibmcnx/member/SyncAllByEXID.py', globdict)

user = ibmcnx.menu.MenuClass.cnxMenu()
# DB2 Driver can't be loaded with WebSphere 8.5.5, so deactivated until
# solution found
user.AddItem('Check External ID (all Apps & Profiles) (ibmcnx/member/CheckExID.py)',
             cnxMemberCheckExIDByEmail)
user.AddItem('Deactivate and Activate a User in one step (ibmcnx/member/DeactAndActByEmail.py)',
             cnxMemberDeactAndActByEmail)
user.AddItem('Deactivate a User by email address (ibmcnx/member/InactivateByEmail.py)',
             cnxMemberInactivateByEmail)
user.AddItem('Deactivate a User by userid (ibmcnx/member/InactivateByUid.py)',
             cnxMemberInactivateByUid)
user.AddItem('Synchronize ExtID for all Users in all Apps (ibmcnx/member/SyncAllByEXID.py)',
             cnxMemberSyncAllByEXID)
user.AddItem('Back to Main Menu (cnxmenu.py)',
             ibmcnx.functions.cnxBackToMainMenu)
user.AddItem("Exit", ibmcnx.functions.bye)

state_user = 'True'
menutitle = "IBM Connections User Admin Tasks"
while state_user == 'True':
    count = len(user.menuitems)
    user.Show(menutitle)

    ###########################
    ## Robust error handling ##
    ## only accept int       ##
    ###########################
    ## Wait for valid input in while...not ###
    is_valid_user = 0
    while not is_valid_user:
        try:
            inputstring = '\tEnter your choice [1-' + str(count) + ']: '
            n = int(raw_input(inputstring))

            if n <= count and n > 0:
                is_valid_user = 1  # set it to 1 to validate input and to terminate the while..not loop
            else:
                print ("'%s' is not a valid menu option.") % n
        except ValueError, e:
            print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
   # n = input( "your choice> " )
    user.Do(n - 1)
