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
#
# To run this script with Windows or SLES, you have to modify setupCmdLine
#
# Windows:
# Create d:\ibm\wasuserscript.cmd:
# "SET WAS_EXT_DIRS=%WAS_EXT_DIRS%;c:\ibm\sqllib\java"
# export WAS_USER_SCRIPT=D:\IBM\wasuserscript.cmd
# start wsadmin
#
# Linux:
# Create /opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wasuserscript.sh
# export WAS_EXT_DIRS=$WAS_EXT_DIRS:/opt/IBM/WebSphere/JDBC
# export WAS_USER_SCRIPT=/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wasuserscript.sh
# start wsadmin

import os
import sys
from java.util import Properties
import ConfigParser

# Only load commands if not initialized directly (call from menu)
if __name__ == "__main__":
    execfile("ibmcnx/loadCnxApps.py")

import com.ibm.db2.jcc.DB2Driver as Driver

# Get configuration from properties file
configParser = ConfigParser.ConfigParser()
configFilePath = r'ibmcnx/ibmcnx.properties'
configParser.read(configFilePath)

# Change User and Password
props = Properties()
props.put( 'user', configParser.get('Database','dbUser') )
props.put( 'password', configParser.get('Database','dbPassword') )

jdbcPath = 'jdbc:db2://' + configParser.get('Database','dbHost') + ':' + configParser.get('Database','dbPort') + '/' + configParser.get('Database','dbName')

conn = Driver().connect( jdbcPath, props )

stmt = conn.createStatement()

email = raw_input( "Mail address of profile you want to check: " ).lower()

sql = 'select PROF_UID_LOWER,PROF_MAIL_LOWER,PROF_GUID,PROF_MAIL from empinst.employee where PROF_MAIL_LOWER = \'' + email + '\' order by PROF_UID_LOWER'
rs = stmt.executeQuery( sql )

employeeList = []
while ( rs.next() ):
    row = {}
    row['PROF_UID_LOWER'] = rs.getString( 1 )
    row['PROF_MAIL_LOWER'] = rs.getString( 2 )
    row['PROF_GUID'] = rs.getString( 3 )
    row['PROF_MAIL'] = rs.getString( 4 )
    employeeList.append( row )

rs.close()
stmt.close()
conn.close()

# print the result
for e in employeeList:
    # print e['PROF_UID_LOWER'] + "\t\t" + e['PROF_MAIL_LOWER'] + "\t\t" + e['PROF_GUID']
    # print e['PROF_MAIL']
    print "Profiles:\t\t\t " + e['PROF_GUID']

try:
    LOGIN = e['PROF_MAIL']
    go_on = 'true'
except:
    print 'No User with mail address ' + email
    go_on = 'false'

if go_on == 'true':
    try:
       print "Activities:\t\t\t",
       ActivitiesMemberService.getMemberExtIdByLogin( LOGIN )
    except:
       print 'No user with Login ' + LOGIN + ' found'
    
    try:
       print "Blogs:\t\t\t\t",
       BlogsMemberService.getMemberExtIdByLogin( LOGIN )
    except:
       print 'No user with Login ' + LOGIN + ' found'
    
    try:
       print "Communities:\t\t\t",
       CommunitiesMemberService.getMemberExtIdByLogin( LOGIN )
    except:
       print 'No user with Login ' + LOGIN + ' found'
    
    try:
       print "Dogear:\t\t\t\t",
       DogearMemberService.getMemberExtIdByLogin( LOGIN )
    except:
       print 'No user with Login ' + LOGIN + ' found'
    
    try:
       print "Files:\t\t\t\t",
       FilesMemberService.getMemberExtIdByLogin( LOGIN )
    except:
       print 'No user with Login ' + LOGIN + ' found'
    
    try:
       print "Forums:\t\t\t\t",
       ForumsMemberService.getMemberExtIdByLogin( LOGIN )
    except:
       print 'No user with Login ' + LOGIN + ' found'
    
    try:
       print "News, Search, Homepage:\t\t",
       NewsMemberService.getMemberExtIdByLogin( LOGIN )
    except:
       print 'No user with Login ' + LOGIN + ' found'
    
    try:
       print "Wikis:\t\t\t\t",
       WikisMemberService.getMemberExtIdByLogin( LOGIN )
    except:
       print 'No user with Login ' + LOGIN + ' found'