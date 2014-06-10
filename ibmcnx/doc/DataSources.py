######
#  Check ExId (GUID) by Email through JDBC
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
#  Check ExId of a User in all Connections Applications

import ibmcnx.functions

dbs = ['FNOSDS', 'FNGCDDS', 'IBM_FORMS_DATA_SOURCE', 'activities', 'blogs', 'communities', 'dogear', 'files', 'forum', 'homepage', 'metrics', 'mobile', 'news', 'oauth provider', 'profiles', 'search', 'wikis']    # List of all databases to check

for db in dbs.splitlines():
    t1 = ibmcnx.functions.getDSId( db )
    AdminConfig.list( t1 )