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
        self.support_group_manager = "N/A"

    #accessors
    def get_ip(self):
        return(self.ip)
    
    def get_sys_class_name(self):
        return(self.sys_class_name)
    
    def get_name(self):
        return(self.name)
    
    def get_fqdn(self):
        return(self.fqdn)
    
    def get_location(self):
        return(self.location)
    
    def get_support_group(self):
        return(self.support_group)
    
    def get_support_group_manager(self):
        return(self.support_group_manager)
    
    #modifiers
    def set_ip(self, ip):
        self.ip = ip
    
    def set_sys_class_name(self, sys_class_name):
        self.sys_class_name = sys_class_name
    
    def set_name(self, name):
        self.name = name
    
    def set_fqdn(self, fqdn):
        self.fqdn = fqdn
    
    def set_location(self, location):
        self.location = location
    
    def set_support_group(self, support_group):
        self.support_group = support_group
    
    def set_support_group_manager(self, support_group_manager):
        self.support_group_manager = support_group_manager
    
#end of class