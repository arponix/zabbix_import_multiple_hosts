#!/usr/bin/env python3

import datetime
import os
import re
import string
import sys
import xml.dom.minidom

from zabbix import Host, Group, Interface, InventoryMode, Export


def read_hosts_file(file_name, group_name):
    try:
        with open(file_name, 'rb') as reader:
            hosts = []
            for line in reader.readlines():
                tokens = line.split()
                groups = [Group(group_name)]
                ip = tokens[0].decode("utf-8")
                host_name = tokens[1].decode("utf-8")
                if not is_ip_address(ip):
                    host_name = tokens[0].decode("utf-8")
                    ip = tokens[1].decode("utf-8")
                    if not is_ip_address(ip):
                        print("[Failed] Invalid IP/Hostname in input file:", line.decode("utf-8"))
                        exit(1)
                host = Host(
                    ip,
                    groups,
                    [Interface(host_name, "if1")],  # todo: change hardcoded reference
                    InventoryMode.DISABLED,
                )
                hosts.append(host)
            export_to_file(os.path.splitext(file_name)[0] + ".xml", hosts)
            export_to_server(hosts)
    except Exception as e:
        print(e)


def is_ip_address(s: string):
    return re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", s)


def export_to_file(file_name, hosts: [Host]):
    try:
        output = os.path.splitext(file_name)[0] + ".xml"
        f = open(output, "w")
        export = Export("5.2", datetime.datetime.now(), hosts[0].groups, hosts)
        f.write(xml.dom.minidom.parseString(str(export)).toprettyxml())
        f.close()
        print("[Success] Zabbix mass export file is created for", len(hosts), "host(s), please check", output)
    except Exception as e:
        print(e)


def export_to_server(hosts: [Host]):
    pass  # todo: this method can be used to call Zabbix API for mass host creation pur pose


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Invalid number of arguments")
    else:
        read_hosts_file(sys.argv[1], sys.argv[2])
