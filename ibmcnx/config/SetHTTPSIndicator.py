'''
Set HTTPSIndicatorHeader for all application server

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       5.0.1
Date:          2024-03-19

License:       Apache 2.0
'''
import ibmcnx.functions


def getAnswer(question):
    answer = ''
    while not answer.isstring():
        answer = raw_input('\t' + question)

    return answer

wasServers = []
wasServers = AdminTask.listServers(
    '[-serverType APPLICATION_SERVER]').splitlines()

print '\n'
timeoutValue = getAnswer(
    "What's the header value for HttpsIndicatorHeader (string)? ")
print '\n'
for wasServer in wasServers:
    tuningVM = AdminConfig.list('TuningParams', wasServer)
    AdminConfig.modify(
        tuningVM, '[[invalidationTimeout "' + timeoutValue + '"]]')
    print "\tSession Timeout set for " + wasServer.split('|')[0].split('(')[0] + ":\t\t" + timeoutValue

print '\n'
ibmcnx.functions.saveChanges()
print '\n'
