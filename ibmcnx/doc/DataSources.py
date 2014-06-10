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

print AdminControl.getCell()
cell = "/Cell:" + AdminControl.getCell() + "/"
cellid = AdminConfig.getid( cell )
dbs = AdminConfig.list( 'DataSource', str(cellid) )

for db in dbs.splitlines().split('('):
    t1 = ibmcnx.functions.getDSId( db )
    AdminConfig.list( t1 )