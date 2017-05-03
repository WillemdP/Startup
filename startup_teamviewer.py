#!/usr/bin/python
import shlex, time
from subprocess import call

DN = open('/dev/null', 'w')
call(shlex.split('nohup ./Desktop/keepAlive.sh 240'), stdout=DN, stderr=DN)
pass
time.sleep(1)






























"""
rFile = open('/etc/teamviewer/global.conf', 'r')
rContent = rFile.readlines()
lineCounter = 0
for line in rContent:
	pos_start = line.find('ClientID')
	if pos_start > 0:
		print 'Found it'
		line = line[:pos_start + 11] + '732782112\n'
		rContent[lineCounter] = line
		break
	lineCounter += 1
rFile.close()

wFile = open('/etc/teamviewer/global.conf', 'w')
for line in rContent:
	wFile.write(line)
wFile.close()
"""

