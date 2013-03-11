#!/usr/bin/env python2.7

""" Takes a nested dict structure and turns it into a list of dicts, 
    merging the old highest-level keys into the lower dicts. 
"""

def dedict(adict, new_key): 
    lst = []
    for k,v in adict.items(): 
        v[new_key] = k
        lst.append(v)
    return lst


