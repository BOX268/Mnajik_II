#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:51:20 2023

@author: thibaud michelet

This is a library that make the linguee python api easy to use

https://github.com/imankulov/linguee-api
this must be installed
"""

import requests


def translateSingleWord(string, src, dest):
    
    api_root = "https://linguee-api.fly.dev/api/v2"
    
    print(string)
    print(src, "to", dest)
    resp = requests.get(f"{api_root}/translations", params={"query": string, "src": src, "dst": dest})

    json = resp.json()
    
    # this is the convoluted path in the json that lead to the list of example phrases
    try :
        examples = json[0]["translations"][0]["examples"]
    
    except :
        examples = []
    
    print(json)
    if (len(json) > 0):
        print(json[0]["translations"][0]["text"])
        return json[0]["translations"][0]["text"], examples
    else:
        return "NA", examples
