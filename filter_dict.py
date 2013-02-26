""" Make a new dict out of an old dict, removing all but the wanted information. 
"""

def filter_dict(old_dict, keep_keys): 
    return {k:v for k,v in old_dict.keys() if k in keep_keys}
