'''
Class for Menus

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.stoeps.de

Version:       @@version@@
Date:          @@date@@

License:       Apache 2.0
'''


class cnxMenu:

    def __init__(self):
        self.menuitems = []

    # Function to add menuitems
    def AddItem(self, text, function):
        self.menuitems.append({'text': text, 'func': function})

    # Function for printing
    def Show(self, menutitle):
        self.c = 1
        print '\n\t' + menutitle
        print '\t----------------------------------------', '\n'
        for self.l in self.menuitems:
            print '\t',
            print self.c, self.l['text']
            self.c += 1
        print

    def Do(self, n):
        self.menuitems[n]["func"]()
