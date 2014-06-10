import ibmcnx.filehandle

emp1 = ibmcnx.filehandle.Ibmcnxfile()

emp1.writeToFile( execfile('ibmcnx/doc/JVMSettings.py' ) )
#emp1.writeToFile("Test2")
#emp1.writeToFile("Test3")
emp1.closeFile()
