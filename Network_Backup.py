import datetime
import pathlib
import os
import netmiko
import getpass
from getpass import getpass
from pathlib import Path
from netmiko import ConnectHandler

u = input("Please provide a username: ")
p = getpass(prompt='Enter your password: ')
cwd = Path.cwd()
f = 'csrBackup.txt'
w = 'w'
file = open(f, w)
ip = '192.168.253.11'
dict1 = {'ip': ip, 'username': u, 'password': p, 'device_type': 'cisco_ios'}
connection = ConnectHandler(**dict1)
output=connection.send_command('show run')
output2=str(datetime.datetime.now())
file.write(output)
file.write(output2)
file.close()
