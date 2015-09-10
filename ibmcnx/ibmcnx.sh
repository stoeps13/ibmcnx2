#!/bin/bash

JDBC_DRIVER=/opt/IBM/jdbc/db2jcc4.jar

if hash rlwrap; then
    rlwrap -r ./wsadmin.sh $@ -javaoption -Dcom.ibm.ws.scripting.classpath=${JDBC_DRIVER}
else
    ./wsadmin.sh $@ -javaoption -Dcom.ibm.ws.scripting.classpath=${JDBC_DRIVER}
fi
