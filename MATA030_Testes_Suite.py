import unittest

from Teste_MATA030 import MATA030

suite = unittest.TestSuite()

suite.addTest(MATA030('teste_MATA030_001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
