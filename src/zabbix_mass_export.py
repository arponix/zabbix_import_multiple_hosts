import datetime
import os
import re
import string
import sys
import xml.dom.minidom

from zabbix import Host, Group, Interface, InventoryMode, Export


class MassExport:

    def execute(self, input_file_name, output_file_name, group_name):
        try:
            with open(input_file_name, 'rb') as reader:
                hosts = []
                for line in reader.readlines():
                    tokens = line.split()
                    groups = [Group(group_name)]
                    ip = tokens[0].decode("utf-8")
                    host_name = tokens[1].decode("utf-8")
                    if not self.is_ip_address(ip):
                        host_name = tokens[0].decode("utf-8")
                        ip = tokens[1].decode("utf-8")
                        if not self.is_ip_address(ip):
                            print("[Failed] Invalid IP/Hostname in input file:", line.decode("utf-8"))
                            sys.exit(1)
                    host = Host(
                        ip,
                        groups,
                        [Interface(host_name, "if1")],  # todo: change hardcoded reference
                        InventoryMode.DISABLED,
                    )
                    hosts.append(host)
            if output_file_name is None:
                self.export_to_file(os.path.splitext(input_file_name)[0] + ".xml", hosts)
            else:
                self.export_to_file(output_file_name, hosts)
        except Exception as e:
            print(e)

    def is_ip_address(self, s: string):
        return re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", s)

    def export_to_file(self, file_name, hosts: [Host]):
        try:
            output = os.path.splitext(file_name)[0] + ".xml"
            f = open(output, "w")
            export = Export("5.2", datetime.datetime.now(), hosts[0].groups, hosts)
            f.write(xml.dom.minidom.parseString(str(export)).toprettyxml())
            f.close()
            print("[Success] Zabbix mass export file is created for", len(hosts), "host(s), please check", output)
        except Exception as e:
            print(e)
