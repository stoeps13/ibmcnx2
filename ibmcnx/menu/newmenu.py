'''
Script to create menues for Community Connections Scripts

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       5.0.1
Date:          09/19/2015

License:       Apache 2.0

'''


def createMenu(menupoints):
    '''
        Function to calculate numbers for all menus

        menupoints ( list of strings )
    '''
    for item in menupoints:
        print item


def main():
    '''
        Main function to create the menu
    '''
    menu = [['Configuration Tasks', 'cfgtasks.py'][
        'B', 'Back to Menu', 'func1'], ['X', 'Exit', 'func2']]

    createMenu(menu)

main()
