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

dbs = AdminConfig.list('DataSource',AdminConfig.getid('/Cell:cnxwas1Cell01/')).splitlines()
dblist = []
for db in dbs:
    db = db.split('(')
    n = 0
    for i in db:
        if n == 0 and i != "DefaultEJBTimerDataSource" and i != 'OTiSDataSource':
            dblist.append(str(i).replace('"',''))
        n += 1
print dblist
# dbs = dbs.split('(')[0]
# print dbs
#  dbs = ['FNOSDS', 'FNGCDDS', 'IBM_FORMS_DATA_SOURCE', 'activities', 'blogs', 'communities', 'dogear', 'files', 'forum', 'homepage', 'metrics', 'mobile', 'news', 'oauth provider', 'profiles', 'search', 'wikis']    # List of all databases to check
#  
#  for db in dbs:
#      t1 = ibmcnx.functions.getDSId( db )
#      AdminConfig.show( t1 )
#      print '\n\n'
#      AdminConfig.showall( t1 )
#      AdminConfig.showAttribute(t1,'statementCacheSize' )
#      AdminConfig.showAttribute(t1,'[statementCacheSize]' )