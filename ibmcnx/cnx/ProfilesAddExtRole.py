'''
Add extended role to a user

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       @@version@@
Date:          @@date@@

License:       Apache 2.0
'''

import sys
import ConfigParser

global globdict
globdict = globals()

def getMailAddress():
    '''
    Ask for mail address to add role

    Returns
        mail - string
    '''
    mail = raw_input('Adding extended role to user (provide mailaddress): ')
    return mail

def main():
    mailAddress = getMailAddress()
    try:
        role = ProfilesService.getRoles( mailAddress )
    except:
        print 'User not found!'

    if role == 'employee':
        ProfilesService.setRole( mailaddress )
    elif role == 'employee.extended':
        print 'User has alreay role: ' + role
    else:
        print 'User not found in peopleDB.'

# Get configuration from properties file
configParser = ConfigParser.ConfigParser()
configFilePath = r'ibmcnx/ibmcnx.properties'
configParser.read(configFilePath)

try:
    # get admin id to check profiles commands
    connadmin = configParser.get('Generic', 'j2ee.cnxadmin').split('|')
except:
    print "Did you rename ibmcnx_sample.properties?"

try:
    # Check if Profiles Scripts are loaded
    temp = ProfilesService.getRolesByUserId( connadmin[0] )
except:
    print "\tLoading Profiles Admin Commands:"
    execfile("profilesAdmin.py")

main()
