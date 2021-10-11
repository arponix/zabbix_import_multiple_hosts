import datetime
from enum import Enum


class Group:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<group>" + self.name + "</group>"


class Interface:
    def __init__(self, ip, reference):
        self.ip = ip
        self.reference = reference

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<interface>" \
               + "<ip>" + self.ip + "</ip>" \
               + "<interface_ref>" + self.reference + "</interface_ref>" \
               + "</interface>"


class InventoryMode(str, Enum):
    ENABLED = "ENABLED",
    DISABLED = "DISABLED"


class Host():
    def __init__(self, name, groups: [Group], interfaces: [Interface], inventory_mode):
        self.name = name
        self.groups = groups
        self.interfaces = interfaces
        self.inventory_mode = inventory_mode

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<host>" \
               + "<host>" + self.name + "</host>" \
               + "<name>" + self.name + "</name>" \
               + "<groups>" + "".join([str(x) for x in self.groups]) + "</groups>" \
               + "<interfaces>" + "".join([str(x) for x in self.interfaces]) + "</interfaces>" \
               + "</host>"


class Export:
    def __init__(self, version, date: datetime, groups: [Group], hosts: [Host]):
        self.version = version
        self.date = date
        self.groups = groups
        self.hosts = hosts

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "<zabbix_export>" \
               + "<version>" + self.version + "</version>" \
               + "<date>" + str(self.date) + "</date>" \
               + "<groups>" + "".join([str(x) for x in self.groups]) + "</groups>" \
               + "<hosts>" + "".join([str(x) for x in self.hosts]) + "</hosts>" \
               + "</zabbix_export>"
