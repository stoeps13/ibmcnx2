'''
Set Reader Roles to Restricted - no anonymous access possible

Description:
Script is tested with HCL Connections 5

Author: Christoph Stoettner
Blog: http://www.stoeps.de
E-Mail:
Documentation: http://scripting101.stoeps.de

Version:       5.0.1
Date:          09/19/2015

License:       Apache 2.0

History:
20131124  Christoph Stoettner     Update with loop and try/except to handle errors, added group support
20140324  Christoph Stoettner     Changed all reader roles to "All authenticated", Ajax proxy security is configured with this role!
20140716  Christoph Stoettner     Set the script to only change reader role
'''

import ibmcnx.functions

apps = AdminApp.list()
appsList = apps.splitlines()
for app in appsList:
    print "Setting Reader Role to Authenticated for %s" % app.upper()
    try:
        AdminApp.edit(app, '[-MapRolesToUsers [["reader" No Yes "" ""] ]]')
        ibmcnx.functions.saveChanges()
    except:
        print "No Reader Role in %s" % app.upper()
