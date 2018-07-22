import os
import unittest

import app

class BaseTests(unittest.TestCase):

    # def setUp(self):
    #     app.config['TESTING'] = True
    #     app.config['DEBUG'] = False
    #     app.config['SECRET_KEY'] = "TcQsWISFjRG4243XobHPIaDxMioisOba"

    #     self.app = app.test_client()

    # def tearDown(self):
    #     pass

    def test_index_page(self):
        response = self.app.
        self.assertEqual(response)

if __name__ == "__main__":
    unittest.main()