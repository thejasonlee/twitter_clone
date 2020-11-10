from flask import Flask
from gritter import app
from forms import SignUpForm
import os
import unittest
import sqlite3


class FlaskTestCase(unittest.TestCase):


    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

    def tearDown(self):
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute("DELETE FROM user WHERE username = '1aron';")
        c.execute("DELETE FROM user WHERE username = '023456789012345678901234567890';")
        c.execute("DELETE FROM post WHERE content = 'test';")
        conn.commit()
        conn.close()


    # Test Response of home route
    def test_route_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check for 'Welcome to the Home Page!' text on this route
    def test_text_on_home_page(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertIn(b'Welcome to the Home Page!', response.data)

    # Test Response of signup route
    def test_route_signup(self):
        tester = app.test_client(self)
        response = tester.get('/signup', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Check for 'Sign Up Now!' text on this route
    def test_text_on_signup_page(self):
        tester = app.test_client(self)
        response = tester.get('/signup')
        self.assertIn(b'Sign Up Now!', response.data)

    # Check form validation when all fields are at min char length of 5 -> should redirect to home page 
    def test_correct_redirect_if_successful_signup_minCharLength(self):
        tester = app.test_client(self)
        response = tester.post('/signup', data = dict(username="1aron", email="badkid@gmail.com", password="abcde", confirmPassword="abcde", SignUpForm=""), follow_redirects=True)
        self.assertIn(b'Welcome to the Home Page!', response.data)

    # Check form validation when username and password fields are at max length of 30 -> should redirect to home page
    def test_correct_redirect_if_successful_signup_maxCharLength(self):
        tester = app.test_client(self)
        response = tester.post('/signup', data = dict(username="023456789012345678901234567890", email="baddude@gmail.com", password="323456789012345678901234567890", confirmPassword="323456789012345678901234567890", SignUpForm=""), 
        follow_redirects=True)
        self.assertIn(b'Welcome to the Home Page!', response.data)

    def test_too_few_chars_user(self):
        tester = app.test_client(self)
        response = tester.post('/signup', data = dict(username='tom', email="goodemail@email.com", password="longenough", confirmPassword="longenough", SignUpForm=""))
        self.assertIn(b'Must be between 5 and 30', response.data)

    def test_too_many_chars_user(self):
        tester = app.test_client(self)
        response = tester.post('/signup', data=dict(username='x' * 31, email="goodemail@email.com", password="longenough", confirmPassword="longenough", SignUpForm=""))
        self.assertIn(b'Must be between 5 and 30', response.data)

    def test_too_few_chars_pw(self):
        tester = app.test_client(self)
        response = tester.post('/signup', data=dict(username='timtom', email="goodemail@email.com", password="pass",
                                                    confirmPassword="pass", SignUpForm=""))
        self.assertIn(b'Must be between 5 and 30', response.data)

    def test_pw_confirm(self):
        tester = app.test_client(self)
        response = tester.post('/signup', data=dict(username="1aron", email="badkid@gmail.com", password="abcde",
                                                    confirmPassword="abcde1", SignUpForm=""), follow_redirects=True)
        self.assertIn(b'Field must be equal to password.', response.data)

    def test_signin_pass(self):
        tester = app.test_client(self)
        response = tester.post('/signin', data=dict(username="jason", password="admin"), follow_redirects=True)
        self.assertIn(b'Hello, jason', response.data)

    def test_signin_fail(self):
        tester = app.test_client(self)
        response = tester.post('/signin', data=dict(username="jason", password="notadmin"), follow_redirects=True)
        self.assertIn(b'Please sign in', response.data)

    def test_post_response(self):
        tester = app.test_client(self)
        response = tester.post('/user/home', data=dict(content="testing response"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_post_content(self):
        tester = app.test_client(self)
        response = tester.post('/user/home', data=dict(content="testing response"), follow_redirects=True)
        self.assertIn(b'testing response', response.data)

  #  def test_instantiatiation_of_new_form(self):
   #     app = Flask(__name__)
    #    with app.test_request_context('/signup'):
     #       form = SignUpForm()
      #  self.assertIsInstance(form, SignUpForm())




if __name__ == '__main__':
    unittest.main()


 
