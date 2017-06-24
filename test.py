# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 11:43:58 2017

@author: chetan
"""

with open('frenchopen.json','r') as file, open('frenchopen2.json','w') as out:
    for line in file:
        if not line.isspace():
            out.write(line)
