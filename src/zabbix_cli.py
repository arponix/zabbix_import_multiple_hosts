#!/usr/bin/env python3
import argparse
import sys

from zabbix_mass_export import MassExport

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Zabbix command line interface')
    parser.add_argument('-i', '--input', help='Input file name which includes hosts name and address', required=True)
    parser.add_argument('-o', "--output", help='Export file name', required=False)
    parser.add_argument('-g', "--group", help='Group name', required=True)

    if len(sys.argv) == 1:
        parser.print_usage(sys.stderr)
        sys.exit(1)
    args = vars(parser.parse_args())

    mass_export = MassExport()
    mass_export.execute(args.get("input"), args.get("output"), args.get("group"))
