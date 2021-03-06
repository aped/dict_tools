""" You have a dict but want to map its 'names' to a different set of names,
    without changing the values. 
""" 


def rekey(to_rekey, newmap): 
    """ Where newmap is a dict itself, from old values to new values, or
        a function.
        Keys in to_rekey with no correlate in the map will be preserved. 
    """
    if issubclass(type(newmap), dict): 
        return {(newmap[k] if k in newmap else k):v for k,v in to_rekey.items()}
    else: 
        return {newmap(k):v for k,v in to_rekey.items()}


def rekey_ugly(to_rekey, newmap): 
    """ Same as above, but with a more functional feel. For fun and
    profit. or something. Misses some functionality. 
    """
    op = "get" if issubclass(type(newmap), dict) else "__call__")
    return {(getattr(newmap, op)(k):v for k,v in to_rekey.items()}
