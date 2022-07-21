#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 19:23:35 2022

@author: ciaranmuir406
"""

import json
import re

# Creates unsorted json file for devices in specified format
def create_new_devices_json(old_file, new_file):
    devices_dict = {"Devices": []}
    device_list = parse_devices(old_file)
    with open(new_file, 'w') as f:
        json.dump(devices_dict, f, indent=4)
        
    with open(new_file, 'r+',) as file:
        devices_data = json.load(file)
        for device in device_list:
            devices_data["Devices"].append(device)
        file.seek(0)
        json.dump(devices_data, file, indent=4)
        
# Returns list of dictionary entries for each device in json file in our new format
def parse_devices(file):
    parsed_file = parse_json_file(file)
    devices = parsed_file['Devices']
    device_list = []
    #print("------------------------------------Creating devices------------------------------------")
    for device in devices:
        name = device['Name']
        device_type = device['Type']
        info = get_info(device['Info'])
        uuid = get_uuid(device['Info'])
        payload = count_sensor_payloads(device)
        dev = {"Name": name, "Type": device_type, "Info": info, "UUID": uuid, "Payload": payload}
        device_list.append(dev)
    return device_list
        
# Takes file created by create_new_devices_json()
def sort_devices(old_file, new_file):
    parsed_file = parse_json_file(old_file)
    devices = parsed_file['Devices']
    devices_dict = {"Devices": []}
    
    with open(new_file, 'w') as f:
        json.dump(devices_dict, f, indent=4)
        
    names = []
    names_dic = {}
    for device in devices:
        names.append(device["Name"])
        names_dic[device["Name"]] = device
    
    names.sort(key=str.lower)
    
    with open(new_file, 'r+',) as file:
        devices_data = json.load(file)
        for name in names:
            devices_data["Devices"].append(names_dic[name])
        file.seek(0)
        json.dump(devices_data, file, indent=4)
    

def get_uuid(info):
    result = re.search('uuid:(.*),', info)
    #print("UUID: ", result.group(1))
    return result.group(1)

def get_info(info):
    result = re.sub('uuid:(.*),', '', info)
    #print("INFO: ", result)
    return result

def count_sensor_payloads(device):
    count = 0
    for sensor in device['Sensors']:
        count = count + sensor['Payload']
    #print("Total sensor payload: ", count)
    return count

def parse_json_file(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data
        
create_new_devices_json('data/devices.json', 'new_devices4.json')
sort_devices('new_devices4.json', 'new_devices5_sorted.json')