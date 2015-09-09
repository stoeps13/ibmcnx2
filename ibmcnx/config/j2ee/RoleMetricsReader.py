'''
Set Metrics Reader in J2EE Security Roles

Description:
You can enable and disable Metrics Reader through J2EE Roles with this script

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       @@version@@
Date:          @@date@@

License:       Apache 2.0

History:
20140225  Christoph Stoettner     Initial Version
20140406  Christoph Stoettner     Bug Fixing Line 37 - 44
'''

import ibmcnx.functions


def printMenu():
    state = ''
    while state != ('ENABLE' or 'DISABLE' or 'EXIT'):
        state = raw_input(
            'Do you want to enable or disable Metrics? (E|D|X)(ENABLE|DISABLE|EXIT)').upper()
        if state == 'E':
            state = 'ENABLE'
            break
        elif state == 'D':
            state = 'DISABLE'
            break
        elif state == 'X':
            state = 'EXIT'
            break
        else:
            continue

    if state == 'ENABLE':
        print 'Enable metrics-reader'
        auth = ''
        while auth != ('Y' or 'YES' or 'N' or 'NO'):
            auth = raw_input(
                'Enable metrics-reader Role for \"All-Authenticated in Realm\"? (Y|N)(YES|NO)').upper()
            if auth == 'Y':
                role_auth = 'No Yes'
                break
            elif auth == 'N':
                role_auth = 'No No'
                break
            else:
                continue
        role_users = raw_input(
            'Enable metrics-reader Role for single Users? (Type casesensitiv uid, empty for none, multiple uids seperate by \"|\")')
        role_groups = raw_input(
            'Enable metrics-reader Role for a Group? (Type casesensitiv Groupname, empty for no groups, multiple Groups seperated by \"|\")')

    elif state == 'DISABLE':
        print 'Disable metrics-reader'
        role_auth = 'No No'
        role_users = ''
        role_groups = ''

    if state != 'EXIT':
        apps = ['Activities', 'Blogs', 'Communities', 'Dogear', 'Files', 'Forums',
                'Homepage', 'News', 'Profiles', 'Search', 'WidgetContainer', 'Wikis']
        for app in apps:
            print "Setting Role for " + app
            AdminApp.edit(app, '[-MapRolesToUsers [["metrics-reader" ' +
                          role_auth + ' "' + role_users + '" "' + role_groups + '" ]]]')


printMenu()
ibmcnx.functions.saveChanges()
