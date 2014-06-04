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

perf = {'activities':{'minConnections':configParser.get('Tuning','opnact.min'), 'maxConnections':configParser.get('Tuning','opnact.max')},
         'blogs':{'minConnections':configParser.get('Tuning','blogs.min'), 'maxConnections':configParser.get('Tuning','blogs.max')},
         'communities':{'minConnections':configParser.get('Tuning','sncomm.min'), 'maxConnections':configParser.get('Tuning','sncomm.max')},
         'dogear':{'minConnections':configParser.get('Tuning','dogear.min'), 'maxConnections':configParser.get('Tuning','dogear.max')},
         'files':{'minConnections':configParser.get('Tuning','files.min'), 'maxConnections':configParser.get('Tuning','files.max')},
         'FNOSDS':{'minConnections':configParser.get('Tuning','fnosds.min'), 'maxConnections':configParser.get('Tuning','fnosds.max')},
         'FNOSDSXA':{'minConnections':configParser.get('Tuning','fnosdsxa.min'), 'maxConnections':configParser.get('Tuning','fnosdsxa.max')},
         'forum':{'minConnections':configParser.get('Tuning','forum.min'), 'maxConnections':configParser.get('Tuning','forum.max')},
         'homepage':{'minConnections':configParser.get('Tuning','homepage.min'), 'maxConnections':configParser.get('Tuning','homepage.max')},
         'metrics':{'minConnections':configParser.get('Tuning','metrics.min'), 'maxConnections':configParser.get('Tuning','metrics.max')},
         'mobile':{'minConnections':configParser.get('Tuning','mobile.min'), 'maxConnections':configParser.get('Tuning','mobile.max')},
         'news':{'minConnections':configParser.get('Tuning','news.min'), 'maxConnections':configParser.get('Tuning','news.max')},
         'profiles':{'minConnections':configParser.get('Tuning','profiles.min'), 'maxConnections':configParser.get('Tuning','profiles.max')},
         'search':{'minConnections':configParser.get('Tuning','search.min'), 'maxConnections':configParser.get('Tuning','search.max')},
         'wikis':{'minConnections':configParser.get('Tuning','wikis.min'), 'maxConnections':configParser.get('Tuning','wikis.max')}}

statementCacheSize = configParser.get('Tuning','statementCache')

print 'DataSource Parameters are set to: '
print 'Database \t statementCacheSize \t minConnections \t maxConnections'
for db in perf.keys():
    print db.upper(),
    if len( db ) < 7:
        print '\t',
    print '\t\t' + str( statementCacheSize ),
    print '\t\t\t' + str( perf[db]['minConnections'] ),
    print '\t\t\t' + str( perf[db]['maxConnections'] )
