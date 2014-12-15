"""
Copyright (C) 2006  Daniel Mikusa

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Changed by Christoph Stoettner 2014/12/14
"""
import sys
"""Menu System

   Author:  Daniel Mikusa <dan@trz.cc>
Copyright:  April 4, 2006

A Menu System is a group of Menu and Choice Object arranged to provide a text
based interface for an end user.  These classes are aimed at making
development of Menu based systems easy and fast.

A Menu System is orgainzed into a heirarchy.  There is a top level Menu object,
which has a set of choices.  Any / All / None of this Menu's Choice objects can
contain sub-menus.  The Menu System heirarchy is extended downward by creating
Menu objects with Choice objects that have sub-menus.  As is natural, each
Choice object can only have one sub-menu, but each Menu can have many Choice
objects.
"""
class Menu:
    """Represents one level of a menu system

    A Menu System consists of one or more Menus.  Each Menu consists of a
    title, choices, and a prompt.  A Menu is required to have a title, a prompt
    and at least one choice.  There is no technical limit to the number of
    choices per menu, but asteticly and organizationally more than 10 will
    likely cause problems and should be divided into sub-menus.

    A Menu object is capable of displaying itself and of retreiving a choice
    from the user.  Both function only needs to be called on the top
    level menu object.  The calls will trickle down to all of the menu object
    beneath it in the heirarchy as needed.
    """
    def __init__(self, title='', choice_list=[], prompt=''):
        """Setup a new menu object

        Allows a new Menu object to be easily created by passing the required
        values into a constructor.  All parameters are optional.

                  title -- Menu object's title
                 prompt -- Menu object's prompt
            choice_list -- List of Choice object for Menu
        """
        self.title = title
        self.choices = choice_list
        self.prompt = prompt

    def __getitem__(self, key):
        """Overloads the [] operator for Menu object to get Choices

        Allows us to select a choice from a Menu object using the [] operator.
        print s['3'].  This is mostly a convenience, mostly.

        Given a string 'x', returns the Choice object that has the selector 'x'.
        """
        if isinstance(key, str) and key in self.choices:
            return self.choices[self.choices.index(key)]

    def __repr__(self):
        """Prints the Menu to Standard Out

        Prints the current Menu and triggers a recursive call to all sub-menus
        that are part of this Menu heirarchy.

        The format for display is as follows:

            TITLE

            choice 1
            choice ...
            choice n

            PROMPT

        A Choice object will handle its own formatting, all that is required is
        to call the Choice object's display function.
        """
        if not self.choices:
            return "Please create some choices for this menu"
        count = len(self.title)
        tmpUnderline = str(count * '=')
        tmp = "\n\t" + self.title + "\n\t" + tmpUnderline + "\n\n"
        for choice in self.choices:
            tmp += "\t%s\n" % str(choice)
        tmp += "\n\t%s" % self.prompt
        return tmp

    def waitForInput(self):
        """Main event loop, progresses indefinitly

        Starts the main event loop for the menu system, which consists of
        getting input from standard input, validating it, and calling the proper
        handler function.  Once the handler function returns we continue
        this process indefinitly.

        This process will loop forever, unless you create a return level / exit
        option for the user.  To return a level, or exit if it is the top level
        just return False from the handler function.
        """
        loop = True
        while loop != False:
            print self,
            # c = sys.stdin.readline().strip()
            c = raw_input().strip()
            if c in self.choices:
                # Do this if there is no sub menu
                if self[c].handler and not self[c].subMenu:
                    loop = self[c].handler(self[c].value)
                # Do this is there is a sub menu
                if self[c].subMenu:
                    self[c].subMenu.waitForInput()
                    if self[c].handler:
                        loop = self[c].handler((hasattr(self[c].subMenu, 'data')) and self[c].subMenu.data or None)


class DataMenu(Menu):
    """A data gathering Menu

    A DataMenu is a specific type of menu used to gather information from
    the user.  This is different from the normal menu in that it allows
    for gathering data instead of making a choice.

    A DataMenu consists of no choices, a title, and a prompt.  The title
    describes the menu to the user and the prompt asks the user for the
    requested information.
    """
    def __init__(self, title='', prompt=''):
        """Setup a new data gathering menu object

        Allows a new DataMenu object to be easily created by passing the required
        values into a constructor.  All parameters are optional.

                  title -- Menu object's title
                 prompt -- Menu object's prompt
        """
        self.title = title
        self.prompt = prompt
        self.data = ''

    def __getitem__(self, key):
        """Overloads the [] operator.  Invalid for a DataMenu object"""
        raise TypeError("unsubscriptable object")

    def __repr__(self):
        """Prints the Menu to Standard Out

        Prints the current Menu and triggers a recursive call to all sub-menus
        that are part of this Menu heirarchy.

        The format for display is as follows:

            TITLE

            PROMPT

        A Choice object will handle its own formatting, all that is required is
        to call the Choice object's display function.
        """

        tmp = "\n%s\n" % self.title
        tmp += "\n%s" % self.prompt
        return tmp

    def waitForInput(self):
        """Gathers the data from the user

        Gather's the data from the user.  The data is saved internally, and is
        accessible through the member object 'data'.

        No filtering is performed on the data.  It is saved exactly as the user
        specifies it.
        """
        print self,
        self.data = sys.stdin.readline()


class Choice:
    """
    Represents a standard Menu option

    Each Menu requires one or more Choices.  A Choice consists of a selector,
    a description, a value, and a sub-menu.  The selector, description, and
    value are required, while the sub-menu is optional.

    The presence of a sub-menu will alter the way the Choice is displayed to
    indicate it is a sub-menu to the end user.

    A Choice object is capable of displaying itself and provides instructions
    on what to do if the Choice object is selected.
    """
    def __init__(self, selector=1, description='',
                        value=None, subMenu=None, handler=None):
        """Setup a new Choice object

        Allows a new Choice object to be easily created by specifying the
        required values to the constructor.  All parameters are optional.

        Here are the parameters:

               selector -- value that a user will enter to select a Choice
            description -- value that explains job this Choice will accomplish.
                  value -- value of the selected Choice.
                subMenu -- the Menu object that will be triggered if this Choice
                           is selected.
                handler -- the function that will be executed if this Choice
                           is selected.

        The handler function will be executed even if the Choice object contains
        a sub-menu.  The handler function will be executed, and then control
        will be switched to the handler function.

        The handler function will be passed a single parameter containing the
        value of the Choice object that was selected.  This can be used to find
        out what choice was selected by the end user.  This value will always
        be a string.

        The handler function should never return 'False' unless the desired
        effect is to either go up one level in the menu heirarchy or exit if it
        is at the top level of the menu heirarchy.  If the handler returns
        anything else it is ignored.  Returning True or None are typically best
        and will keep you at the same menu level, Returning False will return
        one level.
        """
        self.selector = selector
        self.description = description
        self.value = str(value)
        self.subMenu = subMenu
        self.handler = handler

    def __repr__(self):
        """Prints the Choice to Standard Out

        The format for display is as follows:

            SELECTOR.) DESCRIPTION

        If the Choice has a sub-menu it will be displayed as follows:

            SELECTOR.) DESCRIPTION >>

        DO NOT INCLUDE END OF LINE CHARACTERS!
        """
        if self.selector == None or self.description == None:
            return "Menu needs to be defined before it can be printed."
        if not self.subMenu:
            return "%s.) %s" % (self.selector, self.description)
        else:
            return "%s.) %s >>" % (self.selector, self.description)

    def __eq__(self, ch):
        """Overloads the == operator for Choice object

        This allows us to determine if two Choice objects are equal by saying
        choiceA == choiceB.  This is mostly a convenience, mostly.
        """
        if isinstance(ch, str):
            return ch == str(self.selector)


class MenuGenie:
    """Generic Interface for loading and saving Menu Systems.

    Defines an Interface for loading and saving Menu Systems.  This is just
    an Interface, it doesn't define how the Menu System is stored.

    To implement this interface you need to define two functions:  load and
    save.  As you would expect, load will create a menu from permanent storage
    and return the top level Menu object.  Save takes a Menu object as
    a parameter and will write that Menu object and all sub-menus to permanent
    storage.
    """
    def load(self):
        """Load a Menu object from permanent storage

        Load and create a Menu object from permanent storage.  This is simply a
        place holder, and needs to be overloaded in a derived class.  Returns
        a menu object that is loaded.
        """
        raise NotImplementedError("This is an abstract class.  You cannot use it directly")

    def save(self, menu):
        """Writes a Menu object to permanent storage

        Write an existing Menu object and all sub-mens to permenant storage.
        This is simply a place holder, and needs to be overloaded in a derived
        class.  Parameter menu is the menu object to write.
        """
        raise NotImplementedError("This is an abstract class.  You cannot use it directly")
