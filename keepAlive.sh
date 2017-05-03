#!/bin/bash

if [[ $1 == '' ]]
then
tout=10
else
tout=$1
fi

while true
do
res=$(fping -c1 -t500 www.google.com 2>/dev/null)
if [[ $res == '' ]]
then
/etc/init.d/networking restart
echo Had to wake it up >keepAlive.log
fi

idleCheck=$(( $(xprintidle) / 1000 + $tout ))
idleCheckms=$(($idleCheck * 1000))

if (( $(xprintidle) > 600000 ))
then
reboot
fi
echo sleeping...
sleep 30
done
