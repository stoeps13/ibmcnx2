######
#  Work with Libraries - add policies
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

#  TODO: Create a Search Filter to get a list of libraries or Users.

execfile( "filesAdmin.py" )

import sys

def printLibs( libraries ):
    for i in range( len( libraries ) ):
        print str( i ) + '\t',
        print str( round( libraries[i]['maximumSize'] / 1073741824.0, 2 ) ) + ' GB\t',
        print str( round( libraries[i]['percentUsed'], 2 ) ) + ' %\t',
        print str( libraries[i]['id'] ) + '\t',
        print str( libraries[i]['title'] )

def printPolicies( policies ):
    state = ''
    print '# \tmax Size \t\t uuid \t\t\t\t\t title'
    print '----------------------------------------------------------------------------------------------------'
    for i in range( len( policies ) ):
        print str( i ) + '\t' + str( round( policies[i]['maximumSize'] / 1073741824.0, 2 ) ) + ' GB\t\t' + str( policies[i]['id'] ) + '\t\t' + str( policies[i]['title'] )
    print
    return policies

def combineMaps( personalList, communityList ):
    pLen = len( personalList )
    cLen = len( communityList )
    print
    for i in range( pLen ):
       print str( i ) + '\t',
       print str( round( personalList[i]['maximumSize'] / 1073741824.0, 2 ) ) + ' GB\t',
       print str( round( personalList[i]['percentUsed'], 2 ) ) + ' %\t',
       print str( personalList[i]['id'] ) + '\t',
       print str( personalList[i]['title'] )
    print
    for i in range( cLen ):
       print str( i + pLen ) + '\t',
       print str( round( communityList[i]['maximumSize'] / 1073741824.0, 2 ) ) + ' GB\t',
       print str( round( communityList[i]['percentUsed'], 2 ) ) + ' %\t',
       print str( communityList[i]['id'] ) + '\t',
       print str( communityList[i]['title'] )
    print
    return pLen, cLen

def askLibraryType():
    #  Check if Community or Personal Libraries should be searched
    is_valid_lib = 0
    while not is_valid_lib :
        try :
                libask = 'Personal or Community Library? (P|C)'
                libType = raw_input( libask ).lower()

                if libType == 'p':
                    is_valid_lib = 1    #  # set it to 1 to validate input and to terminate the while..not loop
                    return libType
                elif libType == 'c':
                    is_valid_lib = 1    #  # set it to 1 to validate input and to terminate the while..not loop
                    return libType
                else:
                    print ( "'%s' is not a valid menu option." ) % libType
        except ValueError, e :
                print ( "'%s' is not valid." % e.args[0].split( ": " )[1] )

def searchLibrary( libType ):
    if libType == 'p':
        libNameAsk = 'Which User you want to search? (min 1 character)'
        libNameAnswer = raw_input( libNameAsk )
        result = FilesUtilService.filterListByString( FilesLibraryService.browsePersonal( "title", "true", 1, 250 ), "title", ".*" + libNameAnswer + ".*" )
        return result

    elif libType == 'c':
        print libType
    else:
        print ( 'Not a valid library Type!' )

def getLibraryDetails( librarieslist ):
    # result = str( librarieslist )
    result = librarieslist
    counter = result.count( 'id=' )
    print counter
    index = 0
    count = 0
    if ( counter < 1 ):
        print '\n------------------------------------------------------------------'
        print 'There is NO Library with this name\nPlease try again ----------->'
        print '------------------------------------------------------------------\n'
        return ( 0, 0, 0, 0, 0 )
    elif ( counter < 2 ):
        lib_id = result[result.find( 'id=' ) + 3:result.find( 'id=' ) + 39]
        lib_name = result[result.find( 'title=' ) + 6:result.find( 'ownerUserId=' ) - 2]
        return ( lib_id, lib_name, 1 )
    else:
        lib_id = []
        lib_name = []
        numberlist = []
        lib_number = -1
        i = 0
        print 'Result: ' + str( len( result ) )
        print '\nThere are multiple libraries with this name:'
        print '----------------------------------------------'
        for i in range( len( result ) ):
            print str( i ) + '\t' + str( round( result[i]['title'] ) ) + ' '  + str( result[i]['id'] ) + '\t\t' + str( result[i]['name'] )
#          while index < len( result ):
#              index = result.find( '{', index )
#              end = result.find( '{', index + 1 )
#              lib_id.append( result[result.find( 'id=' ) + 3:result.find( 'id=' ) + 39] )
#              lib_name.append( result[result.find( 'title=' ) + 6:result.find( 'ownerUserId=' ) - 2] )
#              numberlist.append( count )
#              if index == -1:
#                  break
#              print lib_name
#              print ( str( count ) + ': ' + lib_name[count] )
#              index += 1
#              count += 1
#          print '----------------------------------------------'
#          go_on = ''
#          while go_on != 'TRUE':
#             lib_number = raw_input( 'Please type the number of the library? ' )
#             try:
#                lib_number = float( lib_number )
#             except ( TypeError, ValueError ):
#                continue
#             if count - 1 >= lib_number >= 0:
#                break
#             else:
#                continue
#          return ( lib_id[int( lib_number )], lib_name[int( lib_number )], 1 )

#  Combine personal and community FilesLibrary List
#  TODO: Change this to a function for searching
#  personalList = FilesLibraryService.browsePersonal( "title", "true", 1, 100 )
#  communityList = FilesLibraryService.browseCommunity( "title", "true", 1, 100 )

LibDetails = getLibraryDetails( searchLibrary( askLibraryType() ) )
print LibDetails
#  pLen, cLen = combineMaps( personalList, communityList )


#  print 'Available Policies: '
#  policies = printPolicies( FilesPolicyService.browse( "title", "true", 1, 25 ) )

#  libraryID = int( raw_input( 'Which library should be changed? (0 - %s) ' % str( pLen + cLen - 1 ) ) )
#  if libraryID >= pLen:
#    libraryID = libraryID - pLen
#    libraryType = 'community'
#  else:
#    libraryType = 'personal'

#  policyID = int( raw_input( 'Which policy do you want to assign? ' ) )

#  if libraryType == 'personal':
#    libraryUUID = personalList[libraryID]['id']
#  elif libraryType == 'community':
#    libraryUUID = communityList[libraryID]['id']
#  else:
#    print "Error can't find Library UUID"

#  policyUUID = policies[policyID]['id']

#  FilesLibraryService.assignPolicy( libraryUUID, policyUUID )
