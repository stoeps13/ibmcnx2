######
#  Print trace settings of all JVM
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Documentation: http://scripting101.stoeps.de
#
#  Version:       2.0
#  Date:          2015-07-28
#
#  License:       Apache 2.0
#

ts = AdminControl.queryNames("type=TraceService,*" )
tss=ts.split()
for trace in tss:
       print trace.split(',')[1].split("=")[1]
       spec = AdminControl.getAttribute( trace, "traceSpecification")
       print spec
