#!/usr/bin/python3

import requests
import json

from cmdb_query import cmdb_query

def main():
    debug = 1
    print("test 2")

    ip_addr = "204.135.8.187"

    fields = '&fields=sys_class_name,name,fqdn,sys_id,location,ip_address,support_group,support_group.manager&display_value=true'

    url = 'https://pdsmdev08.service-now.com/api/x_hclfe_cmdb_api/hardware/by_ip?ip_address=' + ip_addr + fields

    key = {}
    with open('key.json', 'r') as f:
        key = json.load(f)

    print(key['usr'])
    print(key['pwd'])

    headers = {"Accept" : "application/json"}

    http_proxy = "199.82.243.100:3128"
    https_proxy = "199.82.243.100:3128"

    proxyDict = {
        "http" : http_proxy,
        "https" : https_proxy
    }


    # Do the HTTP request
    response = requests.get(url, auth=(key['usr'], key['pwd']), headers=headers, proxies=proxyDict)

    q = cmdb_query()

    

    if(response.status_code != 200):
        print("Not return code 200 ", end=" ")
        print(response.status_code)
        print("Header returned ", end=" ")
        print(response.headers)
        print("Error Response ", end=" ")
        print("{}")
        ##print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
        exit()

    print("Status :", response.status_code, "headers: ", response.headers)
    print("Response : ", end="\n")
    print(response.json())
    tmp = response.json()
    print("---------------------------------\n")
    print(tmp['result']['Hardware Details'][0]['name'])
    print(tmp['result']['Hardware Details'][0]['location'])
    print(tmp['result']['Hardware Details'][0]['support_group'])
    print(tmp['result']['Hardware Details'][0]['support_group.manager'])
    print("---------------------------------\n")
    print("\n\n")
    print("Cookies:", response.cookies)



if __name__ == "__main__":
    main()
#end of program