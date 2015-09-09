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

Version:       5.0
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


def moveCommunitiesToParent(parentUUID, subUUIDList):
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


def createCommunity(name, ownerId):
    '''
    Create a new Community with owners to be parent for subcommunities

    Args
        name(str)
            Name of new Community
        ownerId(str)
            LoginId of Admin, will be Owner too.
    '''
    # Trying without a dsml file, maybe we must provide an empty one
    CommunitiesService.createCommunityWithLoginName(name, owner, 1, '')


def getPersonUUID(person):
    '''
    Get the UUID of Connections people

    Args
        person(str)
            Name of a Connections User

    Returns
        UUID(str)
            UUID of Person
    '''


def removeOriginalOwners(communityUUID):
    '''
    Remove Owners of a Community

    Args
        communityUUID(str)
            UUID of a Community

    Returns
        Success(bool)
            True if successful
    '''


def getAnswer(question, possibleAnswers):
    '''
        Function to create raw_input

        Args
            question(str)
                Question
            possibleAnswers(list)
                List with possibleAnswers, e.g. ['y','n']

        Returns
            Answer(str)
                Answer of your question
    '''
    answer = ''
    n = 1
    maxLen = len(possibleAnswers)

    strAnswer = ''
    for i in possibleAnswers:
        if n == 1:
            strAnswer = '(' + str(i)
        elif n < maxLen:
            strAnswer = strAnswer + '/' + str(i)
        else:
            strAnswer = strAnswer + '/' + str(i) + ') '
        n += 1

    inputQuestion = '\t' + question + ' ' + strAnswer
    while answer not in possibleAnswers:
        answer = raw_input(inputQuestion)
        continue
    print '\n'
    return answer
    # END getAnswer()


def getString(question):
    '''
        Function to create raw_input

        Args
            question(str)
                Question
        Returns
            Answer(str)
                Answer of your question
    '''
    answer = ''

    inputQuestion = '\t' + question + ' '
    answer = raw_input(inputQuestion)
    # print '\n'
    return answer
    # END getAnswer()


def main():
    '''
    Main function

    Ask if Archive Community already created, or a new one should be used
    '''

    print '\nIf asked, please select any server to run the communitiesAdmin script! \n\n'

    # execfile("communitiesAdmin.py")
    posAns = ['y', 'n']
    answer = getAnswer(
        'Did you already created a community to move subs in?', posAns)
    if answer == 'n':
        # Create a new community
        comName = getString('New community name:')
        arcOwner = getString(
            'ShortName/UID of an administrator of the community %s :') % comName
        createCommunity(comName, arcOwner)
    else:
        # Let the user select the community name
        print "Give name of archive community:"
    # END main()


main()
