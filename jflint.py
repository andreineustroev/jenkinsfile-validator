#!/usr/bin/env python3

import urllib.request
import sys

from subprocess import Popen, PIPE

if len(sys.argv) == 1:
    print('Usage: jflint <Jenkinsfile>')
    sys.exit(0)

jenkinsfile = sys.argv[1]

req = urllib.request.urlopen('https://jenkins.cc.naumen.ru/login')
ssh_endpoint = req.headers.get('X-SSH-Endpoint')
ssh_jenkins_host = ssh_endpoint.split(':')[0]
ssh_jenkins_port = ssh_endpoint.split(':')[1]

command = 'ssh -p {port} {host} declarative-linter < {jenkinsfile}'.format(
    port=ssh_jenkins_port,
    host=ssh_jenkins_host,
    jenkinsfile=jenkinsfile
    )

print(command)

ssh = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
ret = ssh.communicate()[0]
if ssh.returncode != 0:
    raise ValueError(ssh.returncode)
