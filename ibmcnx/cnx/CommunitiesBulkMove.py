'''
Create a archiving function for Connections Communities

Description:
Creates new archive Communiy, remove orignal owner of Communities and move to
Archive (BP: Create restricted community to hide from user view)

Idea is to move completed Communities or Communities which are not actually used
out of the view of standard users. So they can be reviewed after 12 or 24 months
and then delete them or wait until somebody provides a way to archive them outside
from IBM Connections

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.org

Version:       2.1
Date:          2015-09-02
License:       Apache 2.0

History:
20150902  Christoph Stoettner  Initial version

'''

def getCommunitiesToMove():
    '''
    Let user select a list of communities (without subcommunities) and
    subcommunities and return their uuid

    Doublecheck that selected communities have no subcommunities

    Args

    Returns

    '''

def getParentCommunity():
    '''
    Let user select the new parent community to move communities in

    Args

    Returns

    '''

def moveSubCommunityToCommunity():
    '''
    Temporarily move SubCommunity to a standalone Community

    Args

    Returns

    '''

def moveCommunitiesToParent( parentUUID, subUUIDList ):
    '''
    Move Communities to a parentCommunity

    Args
        parentUUID(str)
            UUID of parent Community
        subUUIDList(list)
            List of UUIDs of Communities which should be moved to parent
    Returns
        bool
            True if successfully moved
    '''

def createCommunity( name, owner ):
    '''
    Create a new Community with owners to be parent for subcommunities

    Args
        name(str)
            Name of new Community
        owner(list)
            List of one or more Owners
    '''

def getPersonUUID( person ):
    '''
    Get the UUID of Connections people

    Args
        person(str)
            Name of a Connections User

    Returns
        UUID(str)
            UUID of Person
    '''

def removeOriginalOwners( communityUUID ):
    '''
    Remove Owners of a Community

    Args
        communityUUID(str)
            UUID of a Community

    Returns
        Success(bool)
            True if successful
    '''

def main():
    '''
    Main function
    '''

main()
