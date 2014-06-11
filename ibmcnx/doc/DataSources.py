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
# remove unwanted databases
for db in dbs:
    dbname = db.split('(')
    n = 0
    for i in dbname:
        # i is only the name of the DataSource, db is DataSource ID!
        if n == 0 and i != "DefaultEJBTimerDataSource" and i != 'OTiSDataSource':
            dblist.append(str(db).replace('"',''))
        n += 1

dblist.sort()

for db in dblist:
      # print db
      print "AdminConfig.show( db ): "
      AdminConfig.show( db )
      print "AdminConfig.showall( db ): "
      AdminConfig.showall( db )
#      AdminConfig.showAttribute(t1,'statementCacheSize' )
#      AdminConfig.showAttribute(t1,'[statementCacheSize]' )