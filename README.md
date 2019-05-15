# jenkinsfile-validator

Validate Jenkinsfile using jenkins CLI over ssh.

Install
=======

1. You must enable SSHD Jenkins server in secyrity settings. This wrapper support random port.
2. Add you ssh id.pub key to user settings in Jenkins.
3. Create config file in ${HOME}/.jflint. Example:
`{
    "jenkins_host": "https://jenkins.example.org"
}`

Usage
=====
jflint <Jenkinsfile>