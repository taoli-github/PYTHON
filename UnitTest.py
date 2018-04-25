import unittest
import logging


# unit test
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except AttributeError as e:
            logging.info(e)

    def __setattr__(self, key, value):
        self[key] = value


class TestDict(unittest.TestCase):
    def setUp(self):
        print('before test do sth... every func execute once for example connect database etc.')

    @classmethod
    def setUpClass(cls):
        print('before test do sth... setUpClass only execute once')

    def test_init(self):
        d = Dict(a=1,b='test')
        print(type(self))
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, Dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d['key'], 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertTrue(d['key'], 'value')

    @unittest.skip('dont test this func')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        self.skipTest('dont run this')
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def tearDown(self):
        print('after test do sth... for example close database connection etc.')

    @classmethod
    def tearDownClass(cls):
        print('after test do sth... tearDownCls only execute once')


if __name__ == '__main__':
    unittest.main()
