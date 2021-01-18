#!/usr/bin/python3

import requests
import json

class cmdb_query(object):
    """
    query cmdb to determine info of hardware

    sys_class_name //OS
    name //hostname
    fqdn //fully qualified domain name
    location //Data Center info
    ip_address //ip info we orig queried
    support_group //sysadmin pdsm group
    support_group.manager // manager over support group
    """

    #constructor
    def __init__(self, ip="127.0.0.1"):
        self.ip = ip
        self.sys_class_name = "NA"
        self.name = "N/A"
        self.fqdn = "N/A"
        self.location = "N/A"
        self.support_group = "N/A"
        self.support_group.manager = "N/A"
    
    