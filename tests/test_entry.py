import unittest
from unittest import TestCase
import app
from app.api.v1.entry.models import Entry
from app.api.v1.entry.views import entries_list
from app import create_app
import json


class EntryTests(TestCase):
    """This class represents the entry test case"""

    def setUp(self):
        """
        Define test variables and initialize app
        """

        self.app = create_app("testing")
        self.client = self.app.test_client
        self.entry = {
            "date" : "Tue, 24 Jul 2018 11:13:26 GMT",
            "entryId" : 2,
            "title" : "some title",
            "details" : "some details"
        }
        
        self.entries_list = [
            {
                'id' : 1,
                'date' : '2018-4-5', 
                'title' : 'Wakanda forever is stale', 
                'details' : 'I do not feel the vibe anymore'
            },
            {
                'id' : 3,
                'date' : '2018-6-5', 
                'title' : 'Black Widow', 
                'details' : 'Give me one reason to hate her'
            },
        ]        

    def test_create_entry(self):
        response = self.client().post('/api/v1/entries/', data=json.dumps(self.entry))
        self.assertEqual(response.status_code, 201)
        self.assertIn('Entry successfully added', str(response.data))

    def test_api_can_get_all_entries(self):
        response = self.client().get('/api/v1/entries/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('All entries successfully retrieved', str(response.data))


if __name__ == '__main__':
    unittest.main()



