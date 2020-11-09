from flask import Flask
from gritter import app
from forms import SignUpForm
import os
import unittest

class FlaskTestCase(unittest.TestCase):


    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False


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




  #  def test_instantiatiation_of_new_form(self):
   #     app = Flask(__name__)
    #    with app.test_request_context('/signup'):
     #       form = SignUpForm()
      #  self.assertIsInstance(form, SignUpForm())




if __name__ == '__main__':
    unittest.main()


 
