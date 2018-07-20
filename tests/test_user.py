import unittest
from app.api.v1.user.models import User

class MyTests(unittest.TestCase):

    def test_user_creation(self):
        user = User('me', 'prossienakimera@gmail.com', 'pr055y')
        assert user
        #self.assertEqual(user.username, 'prossie', msg="username should be prossie")
        assert user.username is type(str) is not 

if __name__ == '__main__':
    unittest.main()



