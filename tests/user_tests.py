import unittest
from app.api.v1.user.models import User

class MyTests(unittest.TestCase):

    def test_user_creation(self):
        user = User('prossie', 'prossienakimera@gmail.com', '')
        assert user
       
        
if __name__ == '__main__':
    unittest.main()



    #self.assertEqual(user.username, 'prossie', msg="username should be prossie")
