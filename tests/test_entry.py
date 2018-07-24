import unittest
from app.api.v1.entry.models import Entry
import datetime

class UserTests(unittest.TestCase):

    def test_entry_creation(self):
        entry = Entry(2,datetime.datetime.now() , 'my entry', 'some details')
        assert entry
    
    

if __name__ == '__main__':
    unittest.main()



