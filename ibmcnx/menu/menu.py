'''
Menu for Connections Community Scripts

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.org

Version:       @@version@@
Date:          @@date@@

License:       Apache 2.0
'''

import ibmcnx.menusystem as menusystem
import sys
import os
import ibmcnx.functions
import java
from java.lang import String
from java.util import HashSet
from java.util import HashMap

global globdict
globdict = globals()

# Handler functions


def cnxMemberCheckExIDByEmail():
    execfile('ibmcnx/member/CheckExId.py', globdict)


def cnxMemberInactivateByEmail():
    execfile('ibmcnx/member/InactivateByEmail.py', globdict)


def cnxMemberDeactAndActByEmail():
    execfile('ibmcnx/member/DeactAndActByEmail.py', globdict)


def cnxMemberSyncAllByEXID():
    execfile('ibmcnx/member/SyncAllByEXID.py', globdict)


def cnxFilesVersionStamp():
    execfile('ibmcnx/cnx/VersionStamp.py', globdict)


def cnxCommunitiesReparenting():
    execfile('ibmcnx/cnx/CommunitiesReparenting.py', globdict)


def cnxFilesPolicies():
    execfile('ibmcnx/cnx/FilesPolicies.py', globdict)


def cnxLibraryPolicies():
    execfile('ibmcnx/cnx/LibraryPolicies.py', globdict)


def cnxLibraryLarge():
    execfile('ibmcnx/cnx/LibraryListLarge.py', globdict)


def cnxLibrarySizes():
    execfile('ibmcnx/cnx/LibrarySizes.py', globdict)


def docDocumentation():
    print '###########################################################'
    print '#                                                         #'
    print '#         Not implemented in the menu!                    #'
    print '#                                                         #'
    print '#  call with:                                             #'
    print '#  wsadmin.sh -lang jython -f ibmcnx/doc/Documentation.py #'
    print '#                                                         #'
    print '###########################################################'
    # execfile( 'ibmcnx/doc/Documentation.py', globdict )


def done(value):
    return False

# Create Sub Menu Configuration Tasks
lst = []
lst.append(menusystem.Choice(selector=1, value=1, handler=ibmcnx.functions.cfgDataSource,
                             description='Configure DataSources (ibmcnx/config/DataSource.py)'))
lst.append(menusystem.Choice(selector=2, value=2, handler=ibmcnx.functions.cfgJVMHeap,
                             description='JVM Heap Sizes (ibmcnx/config/JVMHeap.py)'))
lst.append(menusystem.Choice(selector=3, value=3, handler=ibmcnx.functions.cfgLogFiles,
                             description='SystemOut/Err Log Size (ibmcnx/config/LogFiles.py)'))
lst.append(menusystem.Choice(selector=4, value=4, handler=ibmcnx.functions.cfgJVMLanguage,
                             description='Log Language to english (ibmcnx/config/JVMLanguage.py)'))
lst.append(menusystem.Choice(selector=5, value=5, handler=ibmcnx.functions.cfgMonitoringPolicy,
                             description='Monitoring Policy (ibmcnx/config/MonitoringPolicy.py)'))
lst.append(menusystem.Choice(selector=6, value=6, handler=ibmcnx.functions.cfgJVMCustProp,
                             description='Custom Parameter for Cache Issues in JVM (ibmcnx/config/JVMCustProp.py)'))
lst.append(menusystem.Choice(selector=7, value=7, handler=ibmcnx.functions.cfgChgDBHost,
                             description='Change database server and port (ibmcnx/config/ChgDBHost.py)'))
lst.append(menusystem.Choice(selector=8, value=8, handler=ibmcnx.functions.cfgClusterMembers,
                             description='Create new Clustermembers (ibmcnx/config/addNode.py)'))
lst.append(menusystem.Choice(selector=9, value=9,
                             handler=ibmcnx.functions.synchAllNodes, description='Synchronize all Nodes'))
lst.append(menusystem.Choice(selector=0, value=0,
                             handler=done, description='Return to Main Menu'))
cfgtasks = menusystem.Menu(title='WebSphere Configuration Tasks',
                           choice_list=lst, prompt='What do you want to do? ')

# Create Sub Menu J2EE Roles Configuration Tasks
lst = []
lst.append(menusystem.Choice(selector=1, value=1, handler=ibmcnx.functions.cfgJ2EERoleBackup,
                             description='Backup J2EE Roles (ibmcnx/config/J2EERoleBackup.py)'))
lst.append(menusystem.Choice(selector=2, value=2, handler=ibmcnx.functions.cfgJ2EERoleRestore,
                             description='Restore J2EE Roles (ibmcnx/config/J2EERoleRestore.py)'))
lst.append(menusystem.Choice(selector=3, value=3, handler=ibmcnx.functions.cfgJ2EERolesRestricted,
                             description='Set CNX J2EE Roles (restricted) (ibmcnx/config/J2EERolesRestricted.py)'))
lst.append(menusystem.Choice(selector=4, value=4, handler=ibmcnx.functions.cfgJ2EERolesUnrestricted,
                             description='Set CNX J2EE Roles (public) (ibmcnx/config/J2EERolesRestricted.py)'))
lst.append(menusystem.Choice(selector=5, value=5, handler=ibmcnx.functions.cfgJ2EERoleGlobalModerator,
                             description='Set J2EE Roles for Moderator Roles (ibmcnx/config/J2EERoleGlobalModerator.py)'))
lst.append(menusystem.Choice(selector=6, value=6, handler=ibmcnx.functions.cfgJ2EERoleMetricsReader,
                             description='Set J2EE Role for Metrics Reader (ibmcnx/config/J2EERoleMetricsReader.py)'))
lst.append(menusystem.Choice(selector=7, value=7, handler=ibmcnx.functions.cfgJ2EERoleMetricsReportRun,
                             description='Set J2EE Role for Metrics Report Run (ibmcnx/config/J2EERoleMetricsReportRun)'))
lst.append(menusystem.Choice(selector=8, value=8, handler=ibmcnx.functions.cfgJ2EERoleSocialMail,
                             description='Set J2EE Role for SocialMail (ibmcnx/config/J2EERoleSocialMail)'))
lst.append(menusystem.Choice(selector=0, value=0,
                             handler=done, description='Return to Main Menu'))
cfgj2eetasks = menusystem.Menu(
    title='J2EE Roles Tasks', choice_list=lst, prompt='What do you want to do? ')

# Create Sub Menu Check Tasks
lst = []
lst.append(menusystem.Choice(selector=1, value=1, handler=ibmcnx.functions.checkAppStatus,
                             description='Check if all Apps are running (ibmcnx/check/AppStatus.py)'))
lst.append(menusystem.Choice(selector=2, value=2, handler=ibmcnx.functions.checkDataSource,
                             description='Check Database connections (ibmcnx/check/DataSource.py)'))
lst.append(menusystem.Choice(selector=0, value=0,
                             handler=done, description='Return to Main Menu'))
checks = menusystem.Menu(
    title='Check Tasks', choice_list=lst, prompt='What do you want to do? ')

# Create Sub Menu User Administration
lst = []
lst.append(menusystem.Choice(selector=1, value=1, handler=cnxMemberCheckExIDByEmail,
                             description='Check External ID (all Apps & Profiles) (ibmcnx/member/CheckExID.py)'))
lst.append(menusystem.Choice(selector=2, value=2, handler=cnxMemberDeactAndActByEmail,
                             description='Deactivate and Activate a User in one step (ibmcnx/member/DeactAndActByEmail.py)'))
lst.append(menusystem.Choice(selector=3, value=3, handler=cnxMemberInactivateByEmail,
                             description='Deactivate a User by email address (ibmcnx/member/InactivateByEmail.py)'))
lst.append(menusystem.Choice(selector=4, value=4, handler=cnxMemberSyncAllByEXID,
                             description='Synchronize ExtID for all Users in all Apps (ibmcnx/member/SyncAllByEXID.py)'))
lst.append(menusystem.Choice(selector=0, value=0,
                             handler=done, description='Return to Main Menu'))
useradmin = menusystem.Menu(
    title='User Admin Tasks', choice_list=lst, prompt='What do you want to do? ')

# Create Sub Menu Connections Administration
lst = []
lst.append(menusystem.Choice(selector=1, value=1, handler=cnxFilesVersionStamp,
                             description='Update VersionStamp (ibmcnx/cnx/VersionStamp.py)'))
lst.append(menusystem.Choice(selector=2, value=2, handler=cnxFilesPolicies,
                             description='Work with Files Policies (ibmcnx/cnx/FilesPolicies.py)'))
lst.append(menusystem.Choice(selector=3, value=3, handler=cnxLibraryPolicies,
                             description='Work with Libraries (ibmcnx/cnx/LibraryPolicies.py)'))
lst.append(menusystem.Choice(selector=4, value=4, handler=cnxLibrarySizes,
                             description='Show Library Sizes (ibmcnx/cnx/LibrarySizes.py)'))
lst.append(menusystem.Choice(selector=5, value=5, handler=cnxLibraryLarge,
                             description='List Libraries with more than 80% Used Space (ibmcnx/cnx/LibrarySizes.py)'))
lst.append(menusystem.Choice(selector=6, value=6, handler=cnxCommunitiesReparenting,
                             description='Reparent/Move Communities (ibmcnx/cnx/CommunitiesReparenting.py)'))
lst.append(menusystem.Choice(selector=0, value=0,
                             handler=done, description='Return to Main Menu'))
comm = menusystem.Menu(title='Connections Administration',
                       choice_list=lst, prompt='What do you want to do? ')

# Create Sub Menu Documentation Tasks
lst = []
lst.append(menusystem.Choice(selector=1, value=1, handler=ibmcnx.functions.docJVMHeap,
                             description='Show JVM Heap Sizes (ibmcnx/doc/JVMHeap.py)'))
lst.append(menusystem.Choice(selector=2, value=2, handler=ibmcnx.functions.docJVMSettings,
                             description='Show JVM Settings (ibmcnx/doc/JVMSettings.py)'))
lst.append(menusystem.Choice(selector=3, value=3, handler=ibmcnx.functions.docLogFiles,
                             description='Show SystemOut/Err Log Sizes (ibmcnx/doc/LogFiles.py)'))
lst.append(menusystem.Choice(selector=4, value=4, handler=ibmcnx.functions.docPorts,
                             description='Show all used ports (ibmcnx/doc/Ports.py)'))
lst.append(menusystem.Choice(selector=5, value=5, handler=ibmcnx.functions.docVariables,
                             description='Show all used variables (ibmcnx/doc/Variables.py)'))
lst.append(menusystem.Choice(selector=6, value=6, handler=ibmcnx.functions.docj2eeroles,
                             description='Show all j2ee roles of inst. applications (ibmcnx/doc/j2eeroles.py)'))
lst.append(menusystem.Choice(selector=7, value=7, handler=ibmcnx.functions.docDataSources,
                             description='Show all datasources and parameters (ibmcnx/doc/DataSources.py)'))
lst.append(menusystem.Choice(selector=8, value=8, handler=docDocumentation,
                             description='Create a file with all documentation (ibmcnx/doc/Documentation.py)'))
lst.append(menusystem.Choice(selector=0, value=0,
                             handler=done, description='Return to Main Menu'))
docs = menusystem.Menu(title='Documentation',
                       choice_list=lst, prompt='What do you want to do? ')

# Create menu with links to submenus
lst = []
lst.append(menusystem.Choice(selector=1, value=1, handler=None,
                             description='Configuration Tasks', subMenu=cfgtasks))
lst.append(menusystem.Choice(selector=2, value=2, handler=None,
                             description='Security Roles Tasks', subMenu=cfgj2eetasks))
lst.append(menusystem.Choice(selector=3, value=3, handler=None,
                             description='Check Tasks', subMenu=checks))
lst.append(menusystem.Choice(selector=4, value=4, handler=None,
                             description='User Admin Tasks', subMenu=useradmin))
lst.append(menusystem.Choice(selector=5, value=5, handler=None,
                             description='Admin Tasks', subMenu=comm))
lst.append(menusystem.Choice(selector=6, value=6, handler=None,
                             description='Documentation', subMenu=docs))
lst.append(menusystem.Choice(selector=0, value=0,
                             handler=done, description='Exit'))

# Creat Menu & Begin Execution
head = menusystem.Menu(title='IBM Connections Community Scripts',
                       choice_list=lst, prompt='What do you want to do? ')

if __name__ == '__main__':
    """If your menu functions are in the same file you must use the if __name__ check
    or it will appear that you menus are executed twice"""
    head.waitForInput()

    """Save Menu To XML"""
    # Save Menu
    #xml = menusystem.XMLMenuGenie('save.xml', 'newmenu')
    # xml.save(head)

    #head2 = xml.load()
    # head2.waitForInput()
