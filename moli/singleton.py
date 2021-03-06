"""
Tool to set singleton
"""
def singleton(cls, *args, **kwargs):
    instances = dict()
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton
