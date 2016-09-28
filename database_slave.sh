#!/bin/sh
mount /app
mount /database
oracledir=$ORACLE_HOME
cd $oracledir
cp -rfp listener.ora.slave listener.ora;cp -rfp tnsnames.ora.slave tnsnames.ora
ifconfig eth0:1 virip1 netmask ns1 up
ifconfig eth0:2 virip2 netmask ns2 up
su - oracle -c "lsnrctl start;dbstart"
