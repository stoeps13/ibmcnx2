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

import ConfigParser

#if __name__ == "__main__":
#    echo "Script directly started"

# Function to get the DataSource ID
def getDSId( dbName ):
    try:
        DSId = AdminConfig.getid( '/DataSource:' + dbName + '/' )
        return DSId
    except:
        print "Error when getting the DataSource ID!"
        pass

configParser = ConfigParser.ConfigParser()
configFilePath = r'ibmcnx/ibmcnx.properties'
configParser.read(configFilePath)

perf = {'activities':{'minConnections':int(configParser.get('Tuning','opnact.min')), 'maxConnections':configParser.get('Tuning','opnact.max')},
         'blogs':{'minConnections':1, 'maxConnections':250},
         'communities':{'minConnections':10, 'maxConnections':200},
         'dogear':{'minConnections':1, 'maxConnections':150},
         'files':{'minConnections':10, 'maxConnections':100},
         'FNOSDS':{'minConnections':75, 'maxConnections':200},
         'FNOSDSXA':{'minConnections':25, 'maxConnections':75},
         'forum':{'minConnections':50, 'maxConnections':100},
         'homepage':{'minConnections':20, 'maxConnections':100},
         'metrics':{'minConnections':1, 'maxConnections':75},
         'mobile':{'minConnections':1, 'maxConnections':100},
         'news':{'minConnections':50, 'maxConnections':75},
         'profiles':{'minConnections':1, 'maxConnections':100},
         'search':{'minConnections':50, 'maxConnections':75},
         'wikis':{'minConnections':1, 'maxConnections':100}}

statementCacheSize = 100    # change to 50 for oracle

print 'DataSource Parameters are set to: '
print 'Database \t statementCacheSize \t minConnections \t maxConnections'
for db in perf.keys():
    print db.upper(),
    if len( db ) < 7:
        print '\t',
    print '\t\t' + str( statementCacheSize ),
    print '\t\t\t' + str( perf[db]['minConnections'] ),
    print '\t\t\t' + str( perf[db]['maxConnections'] )
