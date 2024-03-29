#!/usr/bin/env python3

## import paramiko so we can talk SSH
import paramiko
import os

## shortcut issuing commands to remote
def commandissue(command_to_issue):
  ssh_stdin, ssh_stdout, ssh_stderr = sshsession.exec_command(command_to_issue)
  return ssh_stdout.read()

# my commands

print("Servers available: 10.10.2.3, 10.10.2.4, 10.10.2.5")
ser_ver = input('What is the server IP?: ')
user_name = input('What is the username?: ')
pass_word = input('What is the password?: ')

cmd_1 = input('What is the command you want to pass? ')



sshsession = paramiko.SSHClient()

############# IF YOU WANT TO CONNECT USING UN / PW #############
#sshsession.connect(server, username=username, password=password)
############## IF USING KEYS #################

## mykey is our private key
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

## if we never went to this SSH host, add the fingerprint to the known host file
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

## creds to connect
sshsession.connect(hostname=ser_ver, username=user_name, password=pass_word)

## a simple list of commands to issue across our connection
our_commands = [cmd_1]

## cycle through our commands, and issue them on the far end
for x in our_commands:
 print(commandissue(x).decode('utf-8'))
