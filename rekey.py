""" You have a dict but want to map its 'names' to a different set of names,
    without changing the values. 
""" 


def rekey(to_rekey, newmap): 
    """ Where newmap is a dict itself, from old values to new values, or
        a function.
        Keys in to_rekey with no correlate in the map will be preserved. 
    """
    if hasattr(newmap, "__contains__"): 
        return {newmap[k]:v for k,v in to_rekey if k in newmap else k:v}
    else: 
        return {newmap(k):v for k,v in to_rekey}
