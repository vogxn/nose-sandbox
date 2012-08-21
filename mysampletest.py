import timeit
from time import sleep
from mytestcase import mytestcase
from nose.plugins.attrib import attr

class mysampletest(mytestcase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    @attr(speed="slow")
    @attr(tags=["advanced", "basic"])
    def test_first(self):
        t = timeit.Timer(stmt="lst = ['c' for x in xrange(100)]")
        self.debug(t.timeit())
    
    @attr(speed="fast")
    @attr(tags=["advanced"])
    def test_second(self):
        t = timeit.Timer(stmt="lst = ['c'] * 100")
        self.debug(t.timeit())
