'''
Menu for Community Scripts

Author:        Christoph Stoettner
Mail:          christoph.stoettner@stoeps.de
Documentation: http://scripting101.org

Version:       @@version@@
Date:          @@date@@

License:       Apache 2.0

History:       Changed by Jan Alderlieste
'''

import sys
import os
import ibmcnx.functions
import ibmcnx.menu.MenuClass
import java
from java.lang import String
from java.util import HashSet
from java.util import HashMap

#  Only load commands if not initialized directly (call from menu)
# if __name__ == "__main__":
#    execfile( "ibmcnx/loadCnxApps.py" )

global globdict
globdict = globals()


def cfgWebSessionTimeOut():
    execfile('ibmcnx/config/WebSessionTO.py', globdict)

cfg = ibmcnx.menu.MenuClass.cnxMenu()
cfg.AddItem('Configure DataSources (ibmcnx/config/DataSource.py)',
            ibmcnx.functions.cfgDataSource)
cfg.AddItem('Configure JVM Heap Sizes (ibmcnx/config/JVMHeap.py)',
            ibmcnx.functions.cfgJVMHeap)
cfg.AddItem('Configure SystemOut/Err Log Size (ibmcnx/config/LogFiles.py)',
            ibmcnx.functions.cfgLogFiles)
cfg.AddItem('Configure Log Language to english (ibmcnx/config/JVMLanguage.py)',
            ibmcnx.functions.cfgJVMLanguage)
cfg.AddItem('Configure Monitoring Policy (ibmcnx/config/MonitoringPolicy.py)',
            ibmcnx.functions.cfgMonitoringPolicy)
cfg.AddItem('Set Custom Parameter for Cache Issues in JVM (ibmcnx/config/JVMCustProp.py)',
            ibmcnx.functions.cfgJVMCustProp)
cfg.AddItem('Set jvm Trace Parameter (ibmcnx/config/jvmtrace.py)',
            ibmcnx.functions.cfgjvmtrace)
cfg.AddItem('Set application server websession timeout (ibmcnx/config/WebSessionTO.py)',
            cfgWebSessionTimeOut)
cfg.AddItem('Change database server and port (ibmcnx/config/ChgDBHost.py)',
            ibmcnx.functions.cfgChgDBHost)
cfg.AddItem('Create new Clustermembers for IBM Connections (ibmcnx/config/addNode.py)',
            ibmcnx.functions.cfgClusterMembers)
cfg.AddItem('Synchronize all Nodes', ibmcnx.functions.synchAllNodes)
cfg.AddItem('Back to Main Menu (cnxmenu.py)',
            ibmcnx.functions.cnxBackToMainMenu)
cfg.AddItem("Exit", ibmcnx.functions.bye)

state_cfg = 'True'
menutitle = "IBM Connections Configuration Tasks"

while state_cfg == 'True':
    count = len(cfg.menuitems)
    cfg.Show(menutitle)

    ###########################
    #  # Robust error handling ##
    #  # only accept int       ##
    ###########################
    ## Wait for valid input in while...not ###
    is_valid_cfg = 0
    while not is_valid_cfg:
        try:
            inputstring = '\tEnter your choice [1-' + str(count) + ']: '
            n = int(raw_input(inputstring))

            if n <= (count) and n > 0:
                is_valid_cfg = 1  # set it to 1 to validate input and to terminate the while..not loop
            else:
                print ("'%s' is not a valid menu option.") % n
        except ValueError, e:
            print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
   #  n = input( "your choice> " )
    cfg.Do(n - 1)
