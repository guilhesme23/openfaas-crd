import os


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    names = dict()
    names['var1'] = os.getenv('var1')
    names['var2'] = os.getenv('var2')
    return names
