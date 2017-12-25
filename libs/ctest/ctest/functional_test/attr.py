def attr(*args, **kwargs):
    """Decorator that adds attributes to classes or functions
    for use with the Attribute (-a) plugin.
    """
    def wrap_obj(obj):
        for name in args:
            setattr(obj, name, True)
        for name, value in kwargs.iteritems():
            setattr(obj, name, value)
        return obj
    return wrap_obj
