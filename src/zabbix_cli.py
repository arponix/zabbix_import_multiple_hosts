#!/usr/bin/env python3

import sys

from src.zabbix_mass_export import MassExport

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Invalid number of arguments")
    else:
        mass_export = MassExport()
        mass_export.read_hosts_file(sys.argv[1], sys.argv[2])