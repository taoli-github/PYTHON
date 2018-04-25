import unittest
import time
from UnitTest import TestDict


if __name__ == '__main__':
    suite = unittest.TestSuite()

    tests = [TestDict('test_init'), TestDict('test_key'), TestDict('test_attr'), TestDict('test_keyerror'), TestDict('test_attrerror')]
    suite.addTests(tests)

    with open('test_report.txt', 'a') as f:
        f.write('\n' + time.strftime('%Y-%m-%d %H:%M:%S %p') + '\n')
        # other choice HtmlTestRunner export *.html file
        runner = unittest.TextTestRunner(verbosity=2, stream=f)
        runner.run(suite)
