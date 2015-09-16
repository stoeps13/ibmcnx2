'''
Set WebSession Timeout in all application servers

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       @@version@@
Date:          @@date@@

License:       Apache 2.0
'''
import ibmcnx.functions


def getAnswer(question):
    answer = ''
    while not answer.isnumeric():
        answer = raw_input(question)

    return answer

wasServers = []
wasServers = AdminTask.listServers(
    '[-serverType APPLICATION_SERVER]').splitlines()

timeoutValue = getAnswer(
    "Which value should be set as websession timeout (integer)? ")

for wasServer in wasServers:
    tuningVM = AdminConfig.list('TuningParams', wasServer)
    AdminConfig.modify(
        tuningVM, '[[invalidationTimeout "' + timeoutValue + '"]]')
    print "Session Timeout set for " + wasServer.split('|')[0].split('(')[0] + " to\t\t" + timeoutValue

ibmcnx.functions.saveChanges()
