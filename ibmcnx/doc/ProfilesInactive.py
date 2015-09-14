'''
Print all inactivated users

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       @@version@@
Date:          @@date@@

License:       Apache 2.0

'''
import os
import sys
from java.util import Properties
import ConfigParser

global globdict
globdict = globals()

try:
    import com.ibm.db2.jcc.DB2Driver as Driver
except:
    print "\n\tNo jdbc driver available, start wsadmin with\n"
    print "\t\"-javaoption -Dcom.ibm.ws.scripting.classpath=path/db2jcc4.jar\"\n"
    print "\tSee http://scripting101.org/resources/installing-the-scripts/ for details\n"

# Get configuration from properties file
configParser = ConfigParser.ConfigParser()
configFilePath = r'ibmcnx/ibmcnx.properties'
configParser.read(configFilePath)

# Change User and Password
props = Properties()
props.put('user', configParser.get('Database', 'dbUser'))
props.put('password', configParser.get('Database', 'dbPassword'))

jdbcPath = 'jdbc:db2://' + configParser.get('Database', 'dbHost') + ':' + configParser.get(
    'Database', 'dbPort') + '/' + configParser.get('Database', 'dbName')

conn = Driver().connect(jdbcPath, props)
stmt = conn.createStatement()

# Check column names and calls for this, should return inactive profiles
sql = "SELECT r.PROF_DISPLAY_NAME, r.PROF_MAIL from EMPINST.EMPLOYEE WHERE EMPLOYEE.PROF_STATE = 0"

rs = stmt.executeQuery(sql)

employeeList = []
while (rs.next()):
    row = {}
    row['PROF_DISPLAY_NAME'] = rs.getString(1)
    row['PROF_MAIL'] = rs.getString(2)
    employeeList.append(row)

rs.close()
stmt.close()
conn.close()

# print the result
print '\tInactivated Userprofiles:'
print '\t-------------------------\n'
for e in employeeList:
    print e['PROF_DISPLAY_NAME'] + '\t\t' + e['PROF_MAIL']
