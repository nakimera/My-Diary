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
        self.entryId = 2
        self.entry = {
            "date" : "Tue, 24 Jul 2018 11:13:26 GMT",
            "entryId" : 2,
            "title" : "some title",
            "details" : "some details"
        }     

    def test_create_entry(self):
        response = self.client().post('/api/v1/entries/', data=json.dumps(self.entry))
        self.assertEqual(response.status_code, 201)
        self.assertIn('Entry successfully added', str(response.data))

    def test_cannot_create_entry_with_out_title(self):
        self.entry = {
            "date" : "Tue, 24 Jul 2018 11:13:26 GMT",
            "entryId" : 2,
            "title" : " ",
            "details" : "some details"
        }
        response = self.client().post('/api/v1/entries/', data=json.dumps(self.entry))
        self.assertEqual(response.status_code, 400)
        self.assertIn('Please enter a title', str(response.data))

    def test_cannot_create_entry_with_out_details(self):
        self.entry = {
            "date" : "Tue, 24 Jul 2018 11:13:26 GMT",
            "entryId" : 2,
            "title" : "some title",
            "details" : ""
        }
        response = self.client().post('/api/v1/entries/', data=json.dumps(self.entry))
        self.assertEqual(response.status_code, 400)
        self.assertIn('Please enter details', str(response.data))

    def test_cannot_create_entry_with_out_title(self):
        self.entry = {
            "date" : "Tue, 24 Jul 2018 11:13:26 GMT",
            "entryId" : 2,
            "title" : " ",
            "details" : "some details"
        }
        response = self.client().post('/api/v1/entries/', data=json.dumps(self.entry))
        self.assertEqual(response.status_code, 400)
        self.assertIn('Please enter a title', str(response.data))

    def test_cannot_create_entry_with_out_details(self):
        self.entry = {
            "date" : "Tue, 24 Jul 2018 11:13:26 GMT",
            "entryId" : 2,
            "title" : "some title",
            "details" : ""
        }
        response = self.client().post('/api/v1/entries/', data=json.dumps(self.entry))
        self.assertEqual(response.status_code, 400)
        self.assertIn('Please enter details', str(response.data))

    def test_api_can_get_all_entries(self):
        response = self.client().get('/api/v1/entries/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('All entries successfully retrieved', str(response.data))
        
    def test_api_can_not_get_an_entry_with_an_invalid_id(self):
        response = self.client().get('/api/v1/entries/{}'.format(self.entryId))
        self.assertEqual(response.status_code, 404)
        self.assertIn('Entry not found', str(response.data))

    def test_api_can_get_an_entry_by_Id(self): 
        # create entry       
        rv = self.client().post('/api/v1/entries/', data=json.dumps(self.entry))

        #get entry by entryId
        print(self.entries_list)
        response = self.client().get('/api/v1/entries/{}'.format(self.entryId))
        self.assertEqual(response.status_code, 200)


    def test_api_can_update_an_entry(self):
        pass

if __name__ == '__main__':
    unittest.main()



