import unittest
from app.api.v1.auth.models import User

class UserTests(unittest.TestCase):

    def test_user_creation(self):
        user = User('me', 'prossienakimera@gmail.com', 'pr055y')
        assert user
    


if __name__ == '__main__':
    unittest.main()



