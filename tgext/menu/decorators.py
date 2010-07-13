import sys
from caches import shared_cache, entry

##############################################################################
## Section: The decorator classes
##############################################################################
class menu(object):
    def __init__(self, path, name, extension='html', permission=None, url=None, extras={}, sortorder=999999, right=False):
        self.item = entry(path, name, extension, permission, url, extras, sortorder, right)
        
    def __call__(self, func):
        self.item.func = func
        shared_cache.addEntry(self.item)
        return func

class navbar(menu):
    def __init__(self, path, extension=None, permission=None, url=None, extras={}, sortorder=999999, right=False):
        super(navbar, self).__init__(path, u'navbar', extension, permission, url, extras, sortorder, right)
    
class sidebar(menu):
    def __init__(self, path, extension=None, permission=None, url=None, extras={}, sortorder=999999, right=False):
        super(sidebar, self).__init__(path, u'sidebar', extension, permission, url, extras, sortorder, right)

