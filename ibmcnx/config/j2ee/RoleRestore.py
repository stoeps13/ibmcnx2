######
#  Restore of J2EE Security Roles
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Author:        Martin Leyrer
#  Mail:          leyrer@gmail.com
#  Documentation: http://scripting101.stoeps.de
#
#  Version:       2.1
#  Date:          2015-03-07
#
#  License:       Apache 2.0
#  
# History:
# 20150307  Martin Leyrer       Added/fixed/enhanced documentation and app output.
#                               
#                               


import os
import sys
import ibmcnx.functions

# Restore Security Role from Textfile (created with RoleBackup.py)

path = raw_input( "Path and Folder where the files from 'RoleBackup.py' are stored: " )
ibmcnx.functions.checkBackupPath( path )

def convertFile2Dict( appname, path ):
    # function to convert backup txt files of Security Role Backup to a dictionary
    # print '\tPATH: ' + path
    filename = path + '/' + appname + ".txt"
    myfile = open( filename, 'r' )

    count = 0
    dict = {}

    for line in myfile.readlines():
        # for loop through file to read it line by line
        if ( ':' in line ) and ( count > 12 ):
            value = line.split( ':' )[0]
            # cred = line.split(':')[1].strip('\n')
            cred = line.split( ':' )[1]
            # cred = cred.strip(' ')
            cred = cred.strip()
            if value == "Role":
                role = cred
                dict[role] = {}
            dict[role][value] = cred
        count += 1
    return dict

def setSecurityRoles( dictionary, appName ):
    strRoleChange = '['
    for role in dictionary.keys():
        # Loop through Roles
        strRoleChange += '[\"' + role + '\" '
        strRoleChange += dictionary[role]['Everyone?'] + ' '
        strRoleChange += dictionary[role]['All authenticated?'] + ' '
        strRoleChange += '\"' + dictionary[role]['Mapped users'] + '\" '
        strRoleChange += '\"' + dictionary[role]['Mapped groups'] + '\"] '
    strRoleChange += ']]'
    AdminApp.edit( appName, '[-MapRolesToUsers' + strRoleChange + ']' )
    print "Setting Roles and Users for %s" % appName
    ibmcnx.functions.saveChanges()

apps = AdminApp.list()
appsList = apps.splitlines()
# Test with some Apps:
# appsList = ['Blogs','Activities','Wikis']
# or Single App:
# appsList = ['Blogs']
sure = raw_input( 'Are you sure? All roles will be overwritten! (Yes|No) ' )
allowed_answer = ['yes', 'y', 'ja', 'j']

if sure.lower() in allowed_answer:
    for app in appsList:
        # For testing: set app to example applicatio
        setSecurityRoles( convertFile2Dict( app, path ), app )
        print ("Finished: Restore of security roles for application '%s'." % app)
else:
    print 'Restore canceled!'
