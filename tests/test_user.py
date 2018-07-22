import unittest
from app.api.v1.auth.models import User


class UserTests(unittest.TestCase):

    # def test_index(self):
    #     tester = app.test_client(self)
    #     response = tester.get('/login', content_type='html/text')
    #     self.assertAlmostEqual(response,status_code, 200)

    def test_user_creation(self):
        """GIVEN a User model
        WHEN a new user is created
        THEN check the user instance is created, username, email_address, password
        """

        user = User('prossie', 'prossienakimera@gmail.com', 'pr055y')
        assert user
        assert user.username == 'prossie'
        assert user.email_address == 'prossienakimera@gmail.com'
    


if __name__ == '__main__':
    unittest.main()



