import getpass
import pathlib
import netmiko
from getpass import getpass
from pathlib import Path
from netmiko import ConnectHandler
from netmiko.ssh_exception import AuthenticationException, SSHException, NetmikoTimeoutException

u = input("Please provide a username: ")
p = getpass(prompt='Enter your password: ')
cwd = Path.cwd()
f = 'csrBackup.txt'
w = 'w'
file = open(f, w)
ip = '192.168.253.11'
ciscoDevice = {'ip': ip, 'username': u, 'password': p, 'device_type': 'cisco_ios'}
try:
    connection = ConnectHandler(**ciscoDevice)
except (AuthenticationException):
    print('Authentication failed; connection refused on following device: ' + ciscoDevice['ip'])
except (NetmikoTimeoutException):
    print('The following device has timed out: ' + ciscoDevice['ip'])
except (SSHException):
    print('The device was unable to connect using SSH. Please check your configuration setting on: ' + ciscoDevice['ip'])
except Exception as other_error:
    print('The error' + str(other_error) + 'occurred while attempting to connect to: ' + ciscoDevice['ip'])

output_1 = connection.send_command('show run')
output_2 = connection.send_command('show ip int brief')
print(output_1)
print(output_2)
#output2=str(datetime.datetime.now())
file.write(output_1)
#file.write(output2)
file.close()
