#!/bin/sh
mount /dev/vgstore/lvu1 /u1
mount /dev/vgstore/lvu2 /u2
oracledir=/u2/oracle/product/11.2.0/dbhome_1/network/admin
cd $oracledir
cp -rfp listener.ora.242 listener.ora;cp -rfp tnsnames.ora.242 tnsnames.ora
ifconfig eth0:1 192.168.58.242 netmask 255.255.255.0 up
ifconfig eth0:2 192.168.58.243 netmask 255.255.255.0 up
su - oracle -c "lsnrctl start;dbstart"
