#coding:utf8

'''
Created on 2016-4-14
Flask Test Case
'''
import os
import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        # flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        # os.unlink(flaskr.app.config['DATABASE'])
        os.unlink(flaskr.app.config['DATABASE'])

    def test_login(self, username='admin', password='123456'):
        rv = self.app.post('/login', data=dict(username=username, password=password))
        print type(rv.data)

    # def test_empty_db(self):
    #     rv = self.app.get('/')
    #     assert 'No entries here so far' in rv.data

    def test_add_enty(self):
        self.app.post('/login', data=dict(username='admin', password='123456'))
        rv = self.app.post('/add', data=dict(title='maybe', text='i can do it,only you want'))
        print rv.data



if __name__ == '__main__':
    #unittest的执行顺序竟然是按函数的字母顺序执行的，可以使用suite格式
    suite = unittest.TestSuite()
    suite.addTest(FlaskrTestCase("test_login"))
    # suite.addTest(FlaskrTestCase("test_empty_db"))
    suite.addTest(FlaskrTestCase("test_add_enty"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # unittest.TestCase()
    # unittest.main()