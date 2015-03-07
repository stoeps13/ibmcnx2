######
#  Work with Libraries - show fileSize and used space
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Documentation: http://scripting101.stoeps.de
# 
#  Modifications: Martin Leyrer, leyrer@gmail.com
#
#  Version:       2.1
#  Date:          2015-03-07
#
#  License:       Apache 2.0
#

execfile( "filesAdmin.py" )

import sys
from java.util import HashMap

noresult = 0
maxresults = 250

def askLibraryType():
    #  Check if Community or Personal Libraries should be searched
    is_valid_lib = 0
    while not is_valid_lib :
        try :
                libask = 'Personal, Community Library, Menu or Exit? (P|C|M|X)'
                libType = raw_input( libask ).lower()

                if libType == 'p':
                    is_valid_lib = 1    #  # set it to 1 to validate input and to terminate the while..not loop
                    return libType
                elif libType == 'c':
                    is_valid_lib = 1    #  # set it to 1 to validate input and to terminate the while..not loop
                    return libType
                elif libType == 'm':
                    is_valid_lib = 0
                    execfile( 'ibmcnx/menu/cnxmenu.py' )
                elif libType == 'x':
                    is_valid_lib = 0
                    sys.exit()
                else:
                    print ( "'%s' is not a valid menu option." ) % libType
        except ValueError, e :
                print ( "'%s' is not valid." % e.args[0].split( ": " )[1] )

def getLibraryList( libType ):
    pagecount = 1
    if libType == 'p':
        libList = FilesLibraryService.browsePersonal( "title", "true", pagecount, maxresults )
    elif libType == 'c':
        libList = FilesLibraryService.browseCommunity( "title", "true", pagecount, maxresults )
    else:
        print ( 'Not a valid library Type!' )
    return libList

def searchLibrary( libType ):
    if libType == 'p':
        libNameAsk = 'Which User you want to search? (min 1 character): '
        libNameAnswer = raw_input( libNameAsk )
        # result = FilesUtilService.filterListByString( FilesLibraryService.browsePersonal( "title", "true", 1, 250 ), "title", ".*" + libNameAnswer + ".*" )
        result = FilesUtilService.filterListByString( getLibraryList(libType) , "title", ".*" + libNameAnswer + ".*" )
        print "und gefiltert"
        return result

    elif libType == 'c':
        libNameAsk = 'Which Community Library you want to search? (min 1 character): '
        libNameAnswer = raw_input( libNameAsk )
        result = FilesUtilService.filterListByString( FilesLibraryService.browseCommunity( "title", "true", 1, 250 ), "title", ".*" + libNameAnswer + ".*" )
        return result
    
    else:
        print ( 'Not a valid library Type!' )
        
def getLibraryDetails( librarieslist ):
    # result = str( librarieslist )
    result = librarieslist
    counter = len( result )
    index = 0
    count = 0
    
    if ( counter < 1 ):
        print '\n------------------------------------------------------------------'
        print 'There is NO Library with this name\nPlease try again ----------->'
        print '------------------------------------------------------------------\n'
        return ( 0, 0, 0, 0 )
    elif ( counter < 2 ):
        lib_number = 0
        lib_id = result[lib_number]['id']
        lib_name = result[lib_number]['title']
        lib_policy = result[lib_number]['policyId']
        return ( lib_id, lib_name, lib_policy, 1 )
    else:
        lib_id = []
        lib_name = []
        numberlist = []
        lib_number = -1
        i = 0
        print '\nThere are multiple libraries with this name:'
        print '----------------------------------------------'
        for i in range( len( result ) ):
            print str( i ) + '\t' + result[i]['title']
            i += 1
            count += 1
        print '----------------------------------------------'
        go_on = ''
        while go_on != 'TRUE':
            lib_number = raw_input( 'Please type the number of the library? ' )
            try:
                lib_number = int( lib_number )
            except ( TypeError, ValueError ):
                continue
            if count - 1 >= lib_number >= 0:
               break
            else:
                continue
        lib_id = result[lib_number]['id']
        lib_name = result[lib_number]['title']
        lib_max = result[lib_number]['maximumSize']
        lib_size = result[lib_number]['size']
        lib_used = result[lib_number]['percentUsed']
        return ( lib_id, lib_name, lib_max, lib_size, lib_used, 1 )
        
while noresult != 1:
    lib_id, lib_title, lib_max, lib_size, lib_used, noresult = getLibraryDetails( searchLibrary( askLibraryType() ) )

print "\n\tTitle: \t\t" + str(lib_title)
print "\tmaximumSize: \t" + str( round( lib_max / 1073741824.0 , 2 ) ) + ' GB'
print "\tSize used: \t" +  str( round( lib_size / 1073741824.0 , 2 ) ) + ' GB'
print "\tPercent used: \t" + str(lib_used )
# getLibraryDetails(searchLibrary(askLibraryType()))
