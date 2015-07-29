######
#  set jvm trace 
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Documentation: http://scripting101.stoeps.de
#
#  Version:       2.0
#  Date:          2015-07-28
#
#  License:       Apache 2.0
#

def selectServer( serverlist ):
    result = serverlist
    counter = len( result )
    index = []
    count = 0
    servername = ''
    server_number = 0
    serverselected = []
    i = 0
    print '\n\tAvailable Servers: '
    for i in range( len( result ) ):
        print '\t' + str( i ) + '\t' + result[i].split(',')[1].split('=')[1]
        i += 1
        count += 1
    print '\n'
    go_on = 'FALSE'
    while go_on == 'FALSE':
        if len( serverselected ) >= 0:
            print '\n\t',
            # print serverselected
	    index.sort()
            print 'Selected: ' + str( index )
	    print '\n'
        server_number = raw_input( '\tPlease select the Server where trace settings should be added, (A)ll or End with x: ' )
        # Should add a function which only add the server, when not already in the list
	if ( server_number.lower() != 'x' ) and ( server_number.lower() != 'a' ):
            try:
		index.append( server_number )
                server_number = int( server_number )
                serverselected.append( result[server_number] )
            except ( TypeError, ValueError ):
                continue
        elif server_number.lower() == 'a':
	    serverselected = result
            go_on = 'TRUE'
        elif server_number.lower() == 'x':
            go_on = 'TRUE'

    return ( serverselected )

def getTraceSettings( traceServices ):
    tss = traceServices.split()
    print '\n\t JVM Trace Settings of all servers'
    print '\t =================================\n'
    for trace in tss:
           print '\t ' + str(trace.split(',')[1].split("=")[1])
           spec = AdminControl.getAttribute( trace, "traceSpecification")
           print '\t\t ' + spec + '\n'
    return ( tss )

def resetTraceSettings( traceServices ):
    for traceService in traceServices:
        AdminControl.setAttribute( traceService, "traceSpecification", "*=info=enabled" )
    print "All trace settings set to default *=info"

def setTraceSettings( traceServices, traceString ):
    traceStr = traceString + "=enabled"
    for traceService in traceServices:
        AdminControl.invoke( traceService, "appendTraceString", traceStr )


# Get list of trace object ids and print actual settings
tss = getTraceSettings( AdminControl.queryNames("type=TraceService,*" ) )

answer = raw_input( 'What do you want to do? (S)et a new JVM Trace, (R)eset JVM Trace to default: ' )
allowed_answer = ['s', 'r']

if ( answer.lower() in allowed_answer ):
    if ( answer.lower() == 's' ):
        # Ask for traceSetting
        traceString = raw_input('\n\tPlease provide traceSettings which should be appended to actual parameters\n\te.g."com.lotus.*=all" or "com.ibm.websphere.*=all:com.lotus.*:all":\n\n\t' )
        # Let user select servers to add trace settings
	traceServices = selectServer( tss )
	setTraceSettings( traceServices, traceString )
    elif ( answer.lower() == 'r' ):
	resetTraceSettings( tss )
    else:
        print "\n\tNothing changed"


# finally print settings again
print '\n\n\tTrace is set to: '
print   '\t================\n'
getTraceSettings( AdminControl.queryNames("type=TraceService,*" ) )
