#!/usr/bin/python3

import requests
import json

from cmdb_query import cmdb_query

def main():
    debug = 1
    print("test 2")

    q1 = cmdb_query()
    q1.set_ip("199.81.216.26")
    q1.query_cmdb()

    print(q1.get_fqdn())
    print(q1.get_sys_class_name())
    
    q1.print_cmdb()

    q2 = cmdb_query("199.81.212.9")
    q2.query_cmdb()

    q2.print_cmdb()

if __name__ == "__main__":
    main()
#end of program