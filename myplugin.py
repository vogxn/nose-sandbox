import logging
import unittest
import nose.core
from nose.plugins.base import Plugin
from functools import partial
import sys

def testCaseLogger(message, logger=None):
    if logger is not None:
        logger.debug(message)

class myplugin(Plugin):
    """
    Custom plugin for the mytests to be run using nose
    """
    
    name = "myplugin"
    def configure(self, options, config):
        self.enabled = 1
        self.enableOpt = "--with-myplugin"
        
        if options.debug_log:
            self.debug_stream = logging.FileHandler(options.debug_log) 

        cfg = nose.config.Config()
        cfg.debugLog = self.debug_stream
        self.testrunner = nose.core.TextTestRunner(stream=sys.stdout, descriptions=True, verbosity=2, config=config)
    
    def options(self, parser, env):
        """
        Register command line options
        """
        parser.add_option("--myplugin-log", action="store",
                          default=env.get('DEBUG_LOG', 'debug.log'),
                          dest="debug_log",
                          help="The path to the testcase debug logs [DEBUG_LOG]")
        
        Plugin.options(self, parser, env)
 
    def __init__(self):
        Plugin.__init__(self)
        
    def prepareTestRunner(self, runner):
        return self.testrunner
    
    def wantClass(self, cls):
        if issubclass(cls, unittest.case.TestCase):
            return True
        return None
    
    def loadTestsFromTestCase(self, cls):
        self._injectLogger(cls)
        
    def _injectLogger(self, test):
        testcaselogger = logging.getLogger("myplugin.mytestcase.%s" % test.__name__)
        self.debug_stream.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s"))
        testcaselogger.addHandler(self.debug_stream)
        testcaselogger.setLevel(logging.DEBUG)
        
        setattr(test, "debug", partial(testCaseLogger, logger=testcaselogger))
            
