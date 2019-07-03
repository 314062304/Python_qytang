#!/usr/local/bin/python3
# # -*- coding: UTF-8 -*-
import paramiko

def qytang_ssh(ip, username, password, port=22, cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

if __name__ == '__main__':
    print(qytang_ssh('192.168.2.229', 'root', 'longser%!#'))
    print(qytang_ssh('192.168.2.229', 'root', 'longser%!#', cmd='pwd'))
    # print('网关为：')
    # print(ssh_get_route('192.168.2.229', 'root', 'longser%!#'))