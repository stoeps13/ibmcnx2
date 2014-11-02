######
#  Documentation of DataSources
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Documentation: http://scripting101.org
#
#  Version:       2.0
#  Date:          2014-11-01
#
#  License:       Apache 2.0
#
#  Important DataSource Parameters

import ibmcnx.functions

# Get a list of all DataSources
datasources = AdminConfig.list('DataSource', AdminConfig.getid( '/Cell:'+AdminControl.getCell()+'/' )).splitlines()
# new list for database names
dbList = []

def multiply_tabs(sth, size):
    return ''.join(["%s" % sth for s in xrange(size)])

for datasource in datasources:
    # split DataSource and DataSource ID
    datasource = datasource.split('(')
    ds = datasource[0]
    # Remove Default Datasources
    if ( ds != 'DefaultEJBTimerDataSource' ) and ( ds != 'OTiSDataSource' ):
        # check for " (e.g. "oauth provider)
        if ( len(ds.split('"')) > 1):
            ds = ds.split('"')[1]
        # write datasouce to database list
        dbList.append( ds )
dbList.sort()

parameterList = ['currentSchema','databaseName','driverType','portNumber','resultSetHoldability','serverName']

for count in range(len(dbList)):
    db = dbList[count]
    # Loop through all databases in our dictionary
    print '\n\tDataSource parameters of: ' + db.upper()
    try:
        # get the id of the datasource
        dsid = ibmcnx.functions.getDSId( db )
        properties = AdminConfig.list('J2EEResourceProperty', dsid).splitlines()

        for prop in properties:
            propName = AdminConfig.showAttribute(prop, 'name')
            for para in parameterList:
                if (propName == para):
                    print '\t\t' + propName,
                    print str(multiply_tabs( ' ', 25 - len(propName) )),
                    print AdminConfig.showAttribute(prop,'value')

    except:
        print ' - ERROR'
