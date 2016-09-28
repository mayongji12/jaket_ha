#!/bin/sh
mount  /app
mount /database
oracledir=/u2/oracle/product/11.2.0/dbhome_1/network/admin
cd $oracledir
cp -rfp listener.ora.master listener.ora;cp -rfp tnsnames.ora.master tnsnames.ora
ifconfig eth0:1 virip1 netmask ns1 up
ifconfig eth0:2 virip2 netmask ns2 up
su - oracle -c "lsnrctl start;dbstart"
