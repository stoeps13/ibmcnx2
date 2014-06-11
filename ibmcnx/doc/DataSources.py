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

cell = AdminControl.getCell()
cellname = "/Cell:" + cell + "/"

# Get a list of all databases except DefaultEJBTimerDataSource and OTiSDataSource
dbs = AdminConfig.list('DataSource',AdminConfig.getid(cellname)).splitlines()
dblist = []
for db in dbs:
    db = db.split('(')
    n = 0
    for i in db:
        if n == 0 and i != "DefaultEJBTimerDataSource" and i != 'OTiSDataSource':
            dblist.append(str(i).replace('"',''))
        n += 1

dblist.sort()

for db in dblist:
      t1 = ibmcnx.functions.getDSId( db )
      print t1
#      AdminConfig.show( t1 )
#      print '\n\n'
#      AdminConfig.showall( t1 )
#      AdminConfig.showAttribute(t1,'statementCacheSize' )
#      AdminConfig.showAttribute(t1,'[statementCacheSize]' )