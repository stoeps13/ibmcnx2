######
#  Functions for IBM Connections Community Scripts
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
#  Collection of functions

import os

# Function to get the DataSource ID
def getDSId( dbName ):
    try:
        DSId = AdminConfig.getid( '/DataSource:' + dbName + '/' )
        return DSId
    except:
        print "Error when getting the DataSource ID!"
        pass

# Function to check for a filepath and create it, when not present
def checkBackupPath( path ) :
    try :
        os.makedirs( path )
    except OSError :
        if not os.path.isdir( path ) :
            raise
