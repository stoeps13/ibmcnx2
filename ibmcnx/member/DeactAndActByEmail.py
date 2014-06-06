######
#  Deactivate and activate a user
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
#  on login problems you often need to deactivate and reactivate a user
#  with this script you can do this with one step

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

email = raw_input( "Mail address of profile you want to deactivate: " ).lower()

sql = 'select PROF_UID,PROF_MAIL,PROF_MAIL_LOWER,PROF_GUID from empinst.employee where PROF_MAIL_LOWER = \'' + email + '\' order by PROF_UID_LOWER'
rs = stmt.executeQuery( sql )

employeeList = []
while ( rs.next() ):
    row = {}
    row['PROF_UID'] = rs.getString( 1 )
    row['PROF_MAIL'] = rs.getString( 2 )
    row['PROF_MAIL_LOWER'] = rs.getString( 3 )
    row['PROF_GUID'] = rs.getString( 4 )
    employeeList.append( row )

rs.close()
stmt.close()
conn.close()

# print the result
for e in employeeList:
    # print e['PROF_UID_LOWER'] + "\t\t" + e['PROF_MAIL_LOWER'] + "\t\t" + e['PROF_GUID']
    # print e['PROF_MAIL']
    print 'Deactivate User with ExID: ' + e['PROF_GUID']

try:
    MAILADDRESS = e['PROF_MAIL']
except:
    print 'No User with mail address ' + email + ' found!'

try:
   print "Inactivate Activities ",
   ActivitiesMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate Blogs ",
   BlogsMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate Communities ",
   CommunitiesMemberService.inactivateMemberByEmail( MAILADDRESS.lower() )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate Dogear ",
   DogearMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate Files ",
   FilesMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate Forums ",
   ForumsMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate News, Search, Homepage ",
   NewsMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
   print "Inactivate Wikis ",
   WikisMemberService.inactivateMemberByEmail( MAILADDRESS )
except:
   print 'No user with Email ' + MAILADDRESS + ' found'

try:
    print 'Inactivate Profiles ',
    ProfilesService.inactivateUser( MAILADDRESS )
except:
    print 'No user with Email ' + MAILADDRESS + ' found'

print 'Activate User: '

ProfilesService.activateUserByUserId( e['PROF_GUID'], email = e['PROF_MAIL'], uid = e['PROF_UID'] )
ProfilesService.publishUserData( MAILADDRESS )
