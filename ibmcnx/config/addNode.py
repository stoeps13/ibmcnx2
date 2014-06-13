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
    print nodename
    return ( nodename, 1 )

cell = AdminControl.getCell()
cellname = "/Cell:" + cell + "/"

clusterlist = AdminConfig.list( 'ServerCluster', AdminConfig.getid( cellname ) ).splitlines()

nodelist = AdminTask.listNodes().splitlines()
nodename, nodevalid = selectNode( nodelist )
print nodename
# for cluster in clusterlist:
#     AdminTask.createClusterMember( '[-clusterName Cluster1 -memberConfig [-memberNode cnxwas2Node01 -memberName Cluster1_server2 -memberWeight 2 -genUniquePorts true -replicatorEntry false]]' )
