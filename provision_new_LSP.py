#  This python script makes rest call to Juniper Northstar to create a new LSP
#  usage: python provision_new_LSP.py

import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
import yaml

def import_variables_from_file():
 my_variables_file=open('variables.yml', 'r')
 my_variables_in_string=my_variables_file.read()
 my_variables_in_yaml=yaml.load(my_variables_in_string)
 my_variables_file.close()
 return my_variables_in_yaml

my_variables_in_yaml=import_variables_from_file()

authuser = my_variables_in_yaml['northstar']['username']
authpwd = my_variables_in_yaml['northstar']['password']
url_base = 'http://' + my_variables_in_yaml['northstar']['ip'] + ':8091/NorthStar/API/v2/tenant/'

url = url_base + '1/topology/1/te-lsps'
headers = { 'content-type' : 'application/json'}
payload='''{
    "name": "newlspfrompython",
    "from": {
        "topoObjectType": "ipv4",
        "address": "10.139.10.139"
    },
    "to": {
        "topoObjectType": "ipv4",
        "address": "10.210.10.112"
    },
    "plannedProperties": {
        "bandwidth": "1M",
        "setupPriority": 7,
        "holdingPriority": 7
    }
}'''

q = requests.post(url, headers=headers, auth=(authuser, authpwd), data=payload)
print 'created LSP: ' + q.json()['name']

