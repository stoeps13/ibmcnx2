'''
Check if seedlists are available, seedlists are very important for search

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       @@version@@
Date:          @@date@@

License:       Apache 2.0

'''

# some variable definitions
applications = [activities, blogs, communities, dogear, files, forums, profiles, wikis]
seed_valid = []
seed_error = []

def main():
    # Load Connections Search Commands
    execfile("searchAdmin.py")

    for app in applications:
        '''
        Returncodes of validateSeedlist:
        CLFRW0262I = Successful
        CLFRW0263I = Error
        '''
        try:
            response = SearchService.validateSeedlist( app )
        exception:
            print 'Problem getting seedlist of ' + app

        if response.split(':')[0] == 'CLFRW0262I':
            seed_valid.append( app )
        else:
            seed_error.append( app )

    # Print apps with errors and successful apps
    if len(seed_valid) >= 1:
        print "Seedlist validation successful for: \n"
        for i in seed_valid:
            print "\t" + i

    if len(seed_error) >= 1:
        print "Seedlist with errors: \n"
        for i in seed_error:
            print "\t" + i
            
main()
