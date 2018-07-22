import unittest
from app.api.v1.entry.models import Entry

class UserTests(unittest.TestCase):

    def test_entry_creation(self):
        entry = Entry(2, 'today', 'my entry', 'some details')
        assert entry
    


if __name__ == '__main__':
    unittest.main()



