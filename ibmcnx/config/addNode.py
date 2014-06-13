######
#  Create Cluster Servers for an additional Node
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Documentation: http://scripting101.stoeps.de
#
#  Version:       2.0
#  Date:          2014-06-13
#
#  License:       Apache 2.0
#

def selectNode( nodelist ):
    result = nodelist
    counter = len( result )
    index = 0
    count = 0
    nodename = ''
    node_number = 0
    i = 0
    print '\n\tAvailable Nodes:'
    for i in range( len( result ) ):
        print '\t' + str( i ) + '\t' + result[i]
        i += 1
        count += 1
    print '\n'
    go_on = ''
    while go_on != 'TRUE':
        node_number = raw_input( '\tPlease select the number of the node, \n\twhere new cluster servers should be created: ' )
        try:
            node_number = int( node_number )
        except ( TypeError, ValueError ):
            continue
        if count - 1 >= node_number >= 0:
            break
        else:
            continue
    nodename = result[node_number]
    return ( nodename, 1 )

def selectCluster( clusterlist ):
    result = clusterlist
    counter = len( result )
    index = 0
    count = 0
    clustername = ''
    cluster_number = 0
    clusterselected = []
    i = 0
    print '\n\tAvailable Clusters: '
    for i in range( len( result ) ):
        print '\t' + str( i ) + '\t' + result[i].split('(')[0]
        i += 1
        count += 1
    print '\n'
    go_on = 'FALSE'
    while go_on == 'FALSE':
        if len( clusterselected ) >= 0:
            print '\n\t',
            print clusterselected
            print '\n'
        cluster_number = raw_input( '\tPlease select the Cluster where Servers should be added, End with x: ' )
        if cluster_number != 'x':
            try:
                cluster_number = int( cluster_number )
                clusterselected.append( result[cluster_number].split('(')[0] )
            except ( TypeError, ValueError ):
                continue
        elif cluster_number == 'x':
            go_on = 'TRUE'
            
    return ( clusterselected, 1 )

cell = AdminControl.getCell()
cellname = "/Cell:" + cell + "/"

clusterlist = AdminConfig.list( 'ServerCluster', AdminConfig.getid( cellname ) ).splitlines()

nodelist = AdminTask.listNodes().splitlines()
nodename, nodevalid = selectNode( nodelist )

servercount = raw_input( '\n\tServername will be Clustername_server#, please type # (e.g. 2, 3 or 4)' )

#  selection of clusterlist
clusterlist = selectCluster( clusterlist )

for cluster in clusterlist:
    servername = cluster + '_server' + str( servercount )
    print '\tServer ' + servername + ' will be created: '
    AdminTask.createClusterMember( '[-clusterName ' + cluster + ' -memberConfig [-memberNode ' + nodename + ' -memberName ' + servername + ' -memberWeight 2 -genUniquePorts true -replicatorEntry false]]' )

AdminConfig.save()
