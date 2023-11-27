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
    
    results = Results()
    
    api_root = "https://linguee-api.fly.dev/api/v2"
    
    print("Word to translate :", string)
    print(src, "to", dest)
    resp = requests.get(f"{api_root}/translations", params={"query": string, "src": src, "dst": dest})

    json = resp.json()
    print(json)
    
    if (len(json) == 0):
        results.success = False
        results.error_msg = "Word not found"
        return results
    
    json = json[0]
    
    results.translation = json["translations"][0]["text"]
    # this is the convoluted path in the json that lead to the list of example phrases
    try :
        results.examples = json["translations"][0]["examples"]
    
    except :
        results.examples = []
    
    print(json)
    if (len(json) > 0):
        print(results.translation)
        return results
    else:
        return results


class Results :
    
    def __init__(self) :
        
        self.success = True
        self.translation = ""
        self.examples = ""
        self.error_msg = ""