import sys
from pylons import config
from caches import shared_cache, entry

class menu(object):
    def __init__(self, path, name, extension='html', permission=None, url=None):
        self.item = entry(path, name, extension, permission, url)
        
    def __call__(self, func):
        self.item.func = func
        shared_cache.addEntry(self.item)
        #print dir(func)
        #for i in dir(func):
        #    print '%s: %s' % (i, getattr(func, i))
        #c = config['package'].controllers.root.RootController
        return func

class navbar(menu):
    def __init__(self, path, extension='html', permission=None, url=None):
        super(navbar, self).__init__(path, u'navbar', extension, permission, url)
    
class sidebar(menu):
    def __init__(self, path, extension='html', permission=None, url=None):
        super(sidebar, self).__init__(path, u'sidebar', extension, permission, url)

class sitemap(menu):
    def __init__(self, path, extension='html', permission=None, url=None):
        super(sidebar, self).__init__(path, u'sitemap', extension, permission, url)
