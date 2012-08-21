import timeit
from time import sleep
from mytestcase import mytestcase
from nose.plugins.attrib import attr

class mysampletest(mytestcase):
    
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    @attr(speed=0)
    @attr(tags=["advanced", "basic"])
    def test_first(self):
        t = timeit.Timer(stmt="lst = ['c' for x in xrange(100)]")
        self.debug(t.timeit())
    
    @attr(tags=["advanced"])
    def test_second(self):
        t = timeit.Timer(stmt="lst = ['c'] * 100")
        self.debug(t.timeit())
