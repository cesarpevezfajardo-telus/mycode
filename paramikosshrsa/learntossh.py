#!/usr/bin/env python3

# import paramiko
import paramiko
import os

## shortcut issuing command to remote
def commandissue(command_to_issue):
    ssh_stdin, ssh_stdout, shh_stderr, = sshsession.exec_command(command_to_issue)
    retun ssh_stdout.read()

sshsession = paramiko.SSHClient()
