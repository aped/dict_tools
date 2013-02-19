#!/usr/bin/env python2.7

def dictby(dicts, usekey):
    """ Reforges a list of dicts into a dict of dicts, keyed by the value of 'usekey':
        [{'End Date': 'c', 'Start Date': 'b', 'Event': 'a'}
         {'End Date': 'f', 'Start Date': 'e', 'Event': 'd'}
         {'End Date': 'i', 'Start Date': 'h', 'Event': 'g'}] -> 
        {'a': {'End Date': 'c', 'Start Date': 'b'}, 
         'd': {'End Date': 'f', 'Start Date': 'e'}, 
         'g': {'End Date': 'i', 'Start Date': 'h'}} """
    return {adict[usekey]: {k:adict[k] for k in adict if k is not usekey} for adict in dicts}

